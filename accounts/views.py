from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponse
from django.shortcuts import redirect

@login_required
def redirect_to_home(request):
    return redirect('logged_home')  # Redirect to the view named 'logged_home'

@login_required
def logged_home(request):
    return render(request, 'accounts/home.html')

# User registration
def register(request):
    if request.user.is_authenticated:
        return redirect('logged_home')  # Redirect authenticated users to logged_home

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login')  # Redirect to logged_home after successful registration
    else:
        form = UserRegistrationForm()
        
    return render(request, 'accounts/register.html', {'form': form})

# Logged home view

# User profile view and update
@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid() or user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('logged_home')  # Redirect to the profile view after saving
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'profile_form': profile_form,
        'user_form': user_form
    }
    return render(request, 'accounts/profile.html', context)



def profile_access_view(request):
    # This view shows a message if the user is not authenticated
    return render(request, 'accounts/profile_access_denied.html')