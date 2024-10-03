from django.shortcuts import render
from .models import Course
from .forms import CourseFilterForm
from .ai_utils import *


def course_list(request):
    all_courses = Course.objects.all()
    enrollable_courses = all_courses.filter(enrollable=True)[:5]
    other_courses = all_courses.filter(enrollable=False)
    
    if request.user.is_authenticated:
        user_profile = request.user.profile  # Assuming you have a user profile with certifications
        recommended_courses = recommend_courses(user_profile)[:5]
    else:
        recommended_courses = []  # If the user is not logged in

    form = CourseFilterForm(request.GET or None)
    
    if form.is_valid():
        if form.cleaned_data['platform']:
            other_courses = other_courses.filter(platform=form.cleaned_data['platform'])
        if form.cleaned_data['level']:
            other_courses = other_courses.filter(level=form.cleaned_data['level'])

    context = {
        'recommended_courses': recommended_courses,
        'enrollable_courses': enrollable_courses,
        'other_courses': other_courses,
        'form': form
    }
    return render(request, 'courses/course_list.html', context)

### Enrollable Views

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Module, Content, Assignment, Submission, Test, UserTestResponse, CourseProgress, Profile
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = Module.objects.filter(course=course)
    content = Content.objects.filter(module__in=modules)
    assignment = Assignment.objects.filter(module__in=modules)


    # Fetch the user's progress on the course, ensure it returns a queryset or an empty list
    user_progress = CourseProgress.objects.filter(user=request.user, course=course)

    context = {
        'assignment':assignment,
        'content': content, 
        'course': course,
        'modules': modules,
        'user_progress': user_progress if user_progress.exists() else None,  # Pass an empty list if no progress
    }
    return render(request, 'courses/course_detail.html', context)

from django.http import JsonResponse

@login_required
def load_module_content(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    content = Content.objects.filter(module=module).first()
    assignment = Assignment.objects.filter(module=module).first()
    test = Test.objects.filter(module=module)

    response_data = {
        'title': module.title if module else 'No Content',
        'documentation': content.documentation if content else 'No documentation available.',
        'assignment_id': assignment.id if assignment else None,
        'test_id': test.first().id if test.exists() else None,
    }

    return JsonResponse(response_data)


@login_required
def module_content(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    content = Content.objects.get(module=module)

    # Fetch assignment and test for the module
    assignment = Assignment.objects.filter(module=module).first()
    test = Test.objects.filter(module=module)

    context = {
        'module': module,
        'content': content,
        'assignment': assignment,
        'test': test,
    }
    return render(request, 'courses/module_content.html', context)

@login_required
def course_progress(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = Module.objects.filter(course=course)
    progress = CourseProgress.objects.filter(user=request.user, course=course)

    return render(request, 'courses/course_progress.html', {
        'course': course,
        'modules': modules,
        'progress': progress
    })


def update_course_progress(user, module):
    profile = Profile.objects.get(user=user)

    total_modules = Module.objects.filter(course=module.course).count()
    completed_tests = UserTestResponse.objects.filter(user=user, test__module__course=module.course, is_correct=True).count()
    
    progress_percentage = (completed_tests / total_modules) * 100
    course_progress, created = CourseProgress.objects.get_or_create(user=user, module=module, course=module.course, profile=profile)
    course_progress.progress = progress_percentage
    course_progress.save()



### Submit test

from django.shortcuts import render, get_object_or_404, redirect
from .models import Module, UserTestResponse, CourseProgress, Test, Enrollment
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Check if user is already enrolled in the course
    if Enrollment.objects.filter(user=request.user, course=course).exists():
        messages.info(request, 'You are already enrolled in this course.')
    else:
        # Enroll the user in the course
        Enrollment.objects.create(user=request.user, course=course)
        messages.success(request, f'Successfully enrolled in {course.name}!')

    return redirect('course_detail', course_id=course.id)

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Module, UserTestResponse, CourseProgress, Test
from django.contrib.auth.decorators import login_required

@login_required
def submit_test(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    test = get_object_or_404(Test, module=module)

    if request.method == 'POST':
        answers = request.POST.getlist('answers')
        correct_answers = 0

        for idx, question in enumerate(test.questions.all()):
            is_correct = (question.correct_answer == answers[idx])
            UserTestResponse.objects.create(
                user=request.user,
                question=question,
                user_answer=answers[idx],
                is_correct=is_correct
            )
            if is_correct:
                correct_answers += 1

        # Calculate the score
        score_percentage = (correct_answers / len(test.questions.all())) * 100
        feedback_message = f"You scored {score_percentage:.2f}%!"

        # Return the score and feedback as a JSON response
        return JsonResponse({
            'message': feedback_message,
            'score': score_percentage,
            'total': len(test.questions.all())
        })
        
    # Handle GET request or other logic here...

from django.contrib import messages
### Test Logic

import random

@login_required
def take_test(request, module_id, course_id):
    module = get_object_or_404(Module, id=module_id)
    test_questions = Test.objects.filter(module=module)

    # Fetch wrong answers and attach to questions
    for question in test_questions:
        wrong_answers = question.wrong_answers  # Assuming wrong_answers is stored in a suitable format
        options = [question.correct_answer] + list(wrong_answers)  # Combine correct and wrong answers
        random.shuffle(options)  # Shuffle the answer options
        question.options = options  # Attach the shuffled options to the question

    if request.method == 'POST':
        correct_answers = 0
        for question in test_questions:
            user_answer = request.POST.get(f'answer_{question.id}')
            if user_answer == question.correct_answer:
                correct_answers += 1
            UserTestResponse.objects.create(
                user=request.user,
                test=question,
                user_answer=user_answer,
                is_correct=(user_answer == question.correct_answer)
            )


        if correct_answers == len(test_questions):  # Check if all answers are correct
            update_course_progress(request.user, module)
        
        score_percentage = (correct_answers / len(test_questions)) * 100
        feedback_message = f"You scored {score_percentage:.2f}%!"

        # Use Django messages framework to pass feedback
        messages.add_message(request, messages.INFO, feedback_message)
        messages.add_message(request, messages.INFO, f'Total Questions: {len(test_questions)}. Correct Answers: {correct_answers}.')

        return redirect('course_detail', course_id=course_id)
    
    return render(request, 'courses/take_test.html', {
        'test_questions': test_questions, 
        'module': module, 
        'course_id': course_id
        })



@login_required
def submit_assignment(request, assignment_id, course_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        submission_text = request.POST.get('submission_text')
        submission_file = request.FILES.get('submission_file')
        submission = Submission(
            assignment=assignment,
            user=request.user,
            submission_text=submission_text,
            submission_file=submission_file
        )
        submission.save()
        return JsonResponse({'message': 'Your assignment has been submitted for grading.'})

        # return redirect('course_detail', course_id=course.id)  # Ensure both IDs are passed

    return render(request, 'courses/submit_assignment.html', {'assignment': assignment, 'course_id': course_id})


@login_required
def my_learning(request):
    progress_data = CourseProgress.objects.filter(user=request.user)

    return render(request, 'courses/my_learning.html', {'progress_data': progress_data})
