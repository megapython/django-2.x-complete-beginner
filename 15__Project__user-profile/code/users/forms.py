from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

user = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    model = user
    fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    model = user
    fields = ('username', 'email')
