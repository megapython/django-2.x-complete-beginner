from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import reverse

User = get_user_model()


# Published Manager
class PublishedQuestionManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


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
    objects = models.Manager()  # Default Manager
    published = PublishedQuestionManager()  # Custom Manager


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})


# TODO - Add a model manager for published answers


# Answer
class Answer(models.Model):
    ANSWER_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=ANSWER_STATUS, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'{self.question.title} - Answer by {self.author}'

    def get_absolute_url(self):
        return reverse('answer_detail', kwargs={
            'pk': self.question.pk,
            'a_pk': self.pk
            })
