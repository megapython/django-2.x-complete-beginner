from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Question

from .forms import (
    QuestionCreationForm,
    QuestionUpdateForm,
)

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


# Question Create
@login_required
def question_create(request):
    if request.method == 'POST':
        # Pass data to form
        form = QuestionCreationForm(request.POST)
        if form.is_valid():
            # Create an instance but do not save yet!
            instance = form.save(commit=False)
            # Assign question user to the current user
            instance.author = request.user
            # Save and commit to database
            instance.save()
            # Send a success message
            messages.success(request, 'Question created successfully!')
            # Redirect to the question detail view
            return redirect(reverse('question_detail', args=(instance.id,)))
    else:
        # Send a blank form
        form = QuestionCreationForm()
    context = {
        'form': form
    }
    return render(request, 'djora/question_create.html', context)


# Question Update
@login_required
def question_update(request, pk):
    # Check for valid question
    question = get_object_or_404(Question, pk=pk)
    # Check for valid user
    if question.author == request.user:
        if request.method == 'POST':
            # Pass data to form with instance as the requested question
            form = QuestionUpdateForm(request.POST, instance=question)
            if form.is_valid():
                # Save and commit to database
                instance = form.save()
                # Send success message
                messages.success(request, 'Question updated successfully!')
                # Redirect to the detail view of updated question
                return redirect(reverse('question_detail', args=(instance.id,)))
        else:
            # Pre-fill the form with existing data
            form = QuestionUpdateForm(instance=question)
    else:
        # If current user is not author then raise an error
        raise PermissionDenied
    context = {
        'form': form
    }
    return render(request, 'djora/question_update.html', context)
