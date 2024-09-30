import os
import google.generativeai as genai
from django.shortcuts import render
from courses.models import CourseProgress, UserTestResponse
from django.contrib.auth.decorators import login_required

@login_required
def mentor_page(request):
    user = request.user

    # Fetch the user's course progress
    progress_data = CourseProgress.objects.filter(user=user)

    # Fetch the user's incorrect test responses
    test_responses = UserTestResponse.objects.filter(user=user, is_correct=False)

    # Prepare data for API call
    data = {
        'user_id': user.id,
        'test_responses': [
            {
                'question': response.test.question,
                'user_answer': response.user_answer,
                'correct_answer': response.test.correct_answer,
            }
            for response in test_responses
        ]
    }

    # Configure the AI model
    genai.configure(api_key="AIzaSyBnKNXTQPUyyZYwVqAbeAU4kB7fENEgpdU")

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Start a chat session and get a response
    chat_session = model.start_chat(history=[])
    user_input = "Explain how AI works"  # Replace with dynamic input if needed
    response = chat_session.send_message(user_input)

    # Pass the response text to the template
    ai_response_text = response.text if response else "No response from AI"

    # Render the mentor page with the progress data and AI feedback
    return render(request, 'mentor/mentor_page.html', {
        'profile': user,  # Pass user profile if needed
        'progress': progress_data,  # User's progress
        'test_scores': [],  # Add test scores if available
        'test_analysis': [],  # Add test analysis if available
        'ai_feedback': ai_response_text,  # Pass AI response to the template
    })
