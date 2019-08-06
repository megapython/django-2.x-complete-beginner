from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Question


# Home Page
# def home_page(request):
#     return render(request, 'djora/index.html')

# -----------------------------------------------------------------------
#   QUESTIONS
# -----------------------------------------------------------------------


# Question List / Index Page
def question_list(request):
    # Get questions which are 'published', we don't want 'draft' questions to show up!
    # questions = Question.objects.filter(status='published')

    # Using a custom Model Manager
    questions = Question.published.all()
    context = {
        'questions': questions
    }
    return render(request, 'djora/index.html', context)


# Question Detail
def question_detail(request, pk):
    # Check for valid question
    question = get_object_or_404(Question, pk=pk)
    # Set appropriate context
    if question.author == request.user:
        context = {
            'question': question,
            # Additional buttons only for original author
            'show_buttons': True
        }
    else:
        context = {
            'question': question
        }
    return render(request, 'djora/question_detail.html', context)
