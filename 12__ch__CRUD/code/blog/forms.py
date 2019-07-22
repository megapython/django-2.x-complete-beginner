from django import forms

from .models import Post


# Create a form instance from a model
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)


# Update Form
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)