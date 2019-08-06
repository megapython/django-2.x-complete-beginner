from django import forms
from .models import Question


# Create Question
class QuestionCreationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'status', 'tags']


# Update Question
class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'status', 'tags']
