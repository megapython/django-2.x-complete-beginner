import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User
class MyUser(AbstractUser):
    # Change pk to a unique user ID
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
