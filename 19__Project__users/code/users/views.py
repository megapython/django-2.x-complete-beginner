from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

from .forms import (
    CustomUserCreationForm,
    CustomUserUpdateForm,
    ProfileUpdateForm
)


# Sign Up
def sign_up(request):
    if request.method == 'POST':
        # Get the data
        form = CustomUserCreationForm(request.POST)
        # Check for validity
        if form.is_valid():
            # Save the user
            form.save()
            # Send success message
            messages.success(request, 'Account created successfully!')
            # Redirect to login page
            return redirect('login')
    else:
        # Display a blank form
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)


User = get_user_model()


# Profile
def profile(request, username):
    # Get the requested user
    user = get_object_or_404(User, username=username)
    # Check if the current user is equal to the requested user
    if user == request.user and user.is_authenticated:
        # Set Context
        # Important - Don't set user context key to 'user'
        # Django by default sets a 'user' context to every response!
        context = {
            'my_user': user,
            'show_buttons': True
        }
    else:
        # Disable the show_buttons
        context = {
            'my_user': user
        }
    return render(request, 'users/profile.html', context)


# Profile Update
@login_required
def profile_update(request, username):
    # Get the user
    user = get_object_or_404(User, username=username)
    # Check if the retreived user is same as the requesting user
    if user == request.user:
        if request.method == 'POST':
            # Get the data from the respective forms
            user_form = CustomUserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
            # Check for validity
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                # Send success message
                messages.success(request, 'Profile updated successfully!')
                # Redirect to the updated profile
                return redirect(reverse('profile', args=(user.username,)))
        else:
            # Prefill the forms
            user_form = CustomUserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)
        # Set context
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
    else:
        # If retreived user is not the requesting user, i.e, if the requesting user is not the owner, then raise error
        raise PermissionDenied
    return render(request, 'users/profile_update.html', context)
