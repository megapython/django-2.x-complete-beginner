from django import forms
from .models import Question, Answer


# Create Question
class QuestionCreationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'status']


# Update Question
class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'status']


# Answer
class AnswerCreationForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'status']


# Answer Update
class AnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'status']
