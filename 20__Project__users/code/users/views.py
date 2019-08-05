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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)


User = get_user_model()


# Profile
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if user == request.user:
        context = {
            'user': user,
            'show_buttons': True
        }
    else:
        context = {
            'user': user
        }
    return render(request, 'users/profile.html', context)


# Profile Update
@login_required
def profile_update(request, username):
    user = get_object_or_404(User, username=username)
    if user == request.user:
        if request.method == 'POST':
            user_form = CustomUserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect(reverse('profile', args=(user.username,)))
        else:
            user_form = CustomUserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
    else:
        raise PermissionDenied
    return render(request, 'users/profile_update.html', context)
