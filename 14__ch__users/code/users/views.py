from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def sign_up(request):
    # Check request method
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # Check for form validity
        if form.is_valid():
            # Save user
            form.save()
            # Get user credentials
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authenticate user
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                print(f'User: {username}\tPassword: {raw_password}')
                # Login user
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)
