from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Profile

user = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = user
        fields = ('username', 'email',)


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('username', 'email', 'first_name', 'last_name',)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('age', 'avataar',)
