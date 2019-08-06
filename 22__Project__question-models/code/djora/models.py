from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import reverse


User = get_user_model()


# Question
class Question(models.Model):
    QUESTION_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=QUESTION_STATUS, default='draft')
    has_answers = models.BooleanField(default=False)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
