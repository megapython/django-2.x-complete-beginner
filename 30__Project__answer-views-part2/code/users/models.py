import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


# Custom User
class MyUser(AbstractUser):
    # Change pk to a unique user ID (UUID)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)


# Profile
class Profile(models.Model):
    # One to one relationship with User
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    # Custom fields
    age = models.PositiveIntegerField(blank=True, null=True)
    avataar = models.ImageField(default='default_user.png', upload_to='profile_pics')

    # To create and save profile we will use 'signals'
    # check 'signals.py' and 'apps.py' for further reference

    def __str__(self):
        return f"{self.user.username}'s profile"

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.username})
