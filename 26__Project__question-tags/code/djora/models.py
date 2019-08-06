from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import reverse
from django.utils.text import slugify

from taggit.managers import TaggableManager


User = get_user_model()


# Published Manager
class PublishedQuestionManager(models.Manager):
    def get_queryset(self):
        return super(PublishedQuestionManager, self).get_queryset().filter(status='published')


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
    objects = models.Manager()
    published = PublishedQuestionManager()
    tags = TaggableManager()  # new

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})

    def save(self):
        self.slug = slugify(self.title)
        super(Question, self).save()
