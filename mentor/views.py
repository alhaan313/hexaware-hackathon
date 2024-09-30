import requests
from django.shortcuts import render
from courses.models import CourseProgress, UserTestResponse
from django.contrib.auth.decorators import login_required

@login_required
def mentor_page(request):
    user = request.user

    # Fetch the user's course progress
    progress_data = CourseProgress.objects.filter(user=user)

    # Initialize AI feedback
    ai_feedback = {}

    if request.method == 'POST':  # Check if a user input has been submitted
        user_query = request.POST.get('user_query')  # Get the user's question
        # Prepare data for API call using course progress
        data = {
            'user_id': user.id,
            'question': user_query,  # Include user's question
            'progress_data': [
                {
                    'course_name': progress.course_name,  # Assuming course_name is a field in CourseProgress
                    'status': progress.status,  # Assuming status is a field in CourseProgress
                }
                for progress in progress_data
            ]
        }

        # Define API URL with your API key
        api_key = "AIzaSyBnKNXTQPUyyZYwVqAbeAU4kB7fENEgpdU"  # Replace with your actual API key
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
        
        headers = {
            'Content-Type': 'application/json'  # Ensure to specify content type
        }

        try:
            # Send a request to Gemini AI
            print(f"Sending request to AI with data: {data}")
            response = requests.post(api_url, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            ai_feedback = response.json()  # Get feedback if successful
            print(f"AI response: {ai_feedback}")
        except requests.exceptions.RequestException as e:
            # Log the error or handle it as needed
            print(f"Error contacting Gemini AI: {e}")
            ai_feedback = {'error': 'Could not fetch feedback from the mentor.'}

    # Render the mentor page with the progress data and AI feedback
    return render(request, 'mentor/mentor_page.html', {
        'profile': user,  # Pass user profile if needed
        'progress': progress_data,  # User's course progress
        'ai_feedback': ai_feedback,  # Pass AI feedback to the template
    })
