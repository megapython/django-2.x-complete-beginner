from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.contrib.auth import get_user_model

from taggit.models import Tag

from .models import Question, Answer

from .forms import (
    QuestionCreationForm,
    QuestionUpdateForm,
    AnswerCreationForm,
    AnswerUpdateForm,
    QuickQuestionCreationForm
)

User = get_user_model()

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
    question_list = Question.published.all()[5:]
    recent_question = Question.published.all()[:5]
    # Top Contributors
    top_contributors = User.objects.annotate(num_answers=Count('answer')).order_by('-num_answers')[:5]
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(question_list, 10)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    context = {
        'questions': questions,
        'top_contributors': top_contributors,
        'recent_question': recent_question
    }
    
    # Quick Draft
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Pass data to form
            form = QuickQuestionCreationForm(request.POST)
            if form.is_valid():
                # Create an instance but do not save yet!
                instance = form.save(commit=False)
                # Assign question user to the current user
                instance.author = request.user
                instance.status = 'published'
                # Save and commit to database
                instance.save()
                # Send a success message
                messages.success(request, 'Question created successfully!')
                # Redirect to the question detail view
                return redirect(reverse('question_detail', args=(instance.id,)))
        else:
            # Send a blank form
            form = QuickQuestionCreationForm()
            context = {
                'questions': questions,
                'top_contributors': top_contributors,
                'recent_question': recent_question,
                'form': form
            }
    return render(request, 'djora/index.html', context)


# Question Detail
def question_detail(request, pk):
    # Check for valid question
    question = get_object_or_404(Question, pk=pk)
    related_questions = question.tags.similar_objects()[:5]  # new
    # Set appropriate context
    if question.author == request.user:
        context = {
            'question': question,
            # Additional buttons only for original author
            'show_buttons': True,
            'related_questions': related_questions
        }
    else:
        context = {
            'question': question,
            'related_questions': related_questions
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
            # Save tags, required becuase of (commit=False)
            form.save_m2m()
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


# Question Delete Confirmation
@login_required
def question_delete(request, pk):
    # Check for valid question
    question = get_object_or_404(Question, pk=pk)
    related_questions = question.tags.similar_objects()[:5]
    # Check for valid user
    if question.author == request.user:
        context = {
            'question': question,
            'related_questions': related_questions
        }
        # Check if the user actually wants to delete the question before actually deleting
        return render(request, 'djora/question_delete.html', context)
    else:
        # If current user is not author then raise an error
        raise PermissionDenied


# Question Delete
@login_required
def question_delete_confirm(request, pk):
    # Check for valid question
    question = get_object_or_404(Question, pk=pk)
    # Check for valid user
    if question.author == request.user:
        # Delete the question
        question.delete()
        # Send a success message for deletion
        messages.success(request, 'Question deleted successfully!')
        # Redirect to our home page
        return redirect('home')
    else:
        # If current user is not author then raise an error
        raise PermissionDenied


# -----------------------------------------------------------------------
#   TAGS
# -----------------------------------------------------------------------

# Tag List
def question_list_tags(request, tag_slug=None):
    # Get all the published questions
    questions = Question.published.all()
    recent_question = Question.published.all()[:5]
    top_contributors = User.objects.annotate(num_answers=Count('answer')).order_by('-num_answers')[:5]
    tag = None

    if tag_slug:
        # Get retreive the tag
        tag = get_object_or_404(Tag, slug=tag_slug)
        # Get all the questions with our tag
        question_list = questions.filter(tags__in=[tag])
        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(question_list, 10)
        try:
            questions = paginator.page(page)
        except PageNotAnInteger:
            questions = paginator.page(1)
        except EmptyPage:
            questions = paginator.page(paginator.num_pages)

    context = {
        'questions': questions,
        'tag': tag,
        'recent_question': recent_question,
        'top_contributors': top_contributors
    }
    return render(request, 'djora/index_tags.html', context)


# -----------------------------------------------------------------------
#   ANSWERS
# -----------------------------------------------------------------------

# Answer List
def answer_list(request, pk):
    # Check for a valid question
    question = get_object_or_404(Question, pk=pk)
    related_questions = question.tags.similar_objects()[:5]
    # Get all the related answers which are published
    answers = Answer.objects.filter(question=question, status='published')
    context = {
        'question': question,
        'answers': answers,
        'related_questions': related_questions
    }
    return render(request, 'djora/answer_list.html', context)


# Answer Detail
def answer_detail(request, pk, a_pk):
    # Check if the question exists
    question = get_object_or_404(Question, pk=pk)
    related_questions = question.tags.similar_objects()[:5]
    # Check if the answer exists
    answer = get_object_or_404(Answer, pk=a_pk)
    answers_count = Answer.objects.filter(question=question, status='published').exclude(id=answer.id).count()
    # Set context depending on the user
    if answer.author == request.user:
        context = {
            'question': question,
            'answer': answer,
            'answers_count': answers_count,
            'related_questions': related_questions,
            # Additional buttons only for original author
            'show_buttons': True
        }
    else:
        context = {
            'question': question,
            'answer': answer,
            'answers_count': answers_count,
            'related_questions': related_questions
        }
    return render(request, 'djora/answer_detail.html', context)


# Answer Create
@login_required
def answer_create(request, pk):
    # Check for a valid question
    question = get_object_or_404(Question, pk=pk)
    related_questions = question.tags.similar_objects()[:5]
    if request.method == 'POST':
        # Pass data to form
        form = AnswerCreationForm(request.POST)
        if form.is_valid():
            # Do not save the form yet!
            instance = form.save(commit=False)
            # Set instance parameters -
            # Set author of answer
            instance.author = request.user
            # Link the question
            instance.question = question
            # Set variable
            if not instance.question.has_answers and instance.status == 'published':
                instance.question.has_answers = True
            # Finally save the instance and commit to database
            instance.save()
            # Send a success message
            messages.success(request, 'Answer created successfully!')
            # Redirect to the detail view of newly created answer
            return redirect(reverse('answer_detail', args=(instance.question.pk, instance.pk,)))
    else:
        # Send a blank form
        form = AnswerCreationForm()
    context = {
        'form': form,
        'question': question,
        'related_questions': related_questions
    }
    return render(request, 'djora/answer_create.html', context)


# Answer Update
@login_required
def answer_update(request, pk, a_pk):
    # Check if the question exists
    question = get_object_or_404(Question, pk=pk)
    related_questions = question.tags.similar_objects()[:5]
    # Check if the answer exists
    answer = get_object_or_404(Answer, pk=a_pk)
    # Check for authorized user
    if answer.author == request.user:
        if request.method == 'POST':
            # Send data and requested answer
            form = AnswerUpdateForm(request.POST, instance=answer)
            if form.is_valid():
                # Save the updated answer
                instance = form.save(commit=False)
                # Update the related question
                if instance.status == 'published':
                    if not instance.question.has_answers:
                        instance.question.has_answers = True
                # Save and commit the updated answer
                instance.save()
                # Send success message
                messages.success(request, 'Answer updated successfully!')
                return redirect(reverse('answer_detail', args=(instance.question.pk, instance.pk,)))
        else:
            form = AnswerUpdateForm(instance=answer)
    else:
        # If current user is not author then raise an error
        raise PermissionDenied
    context = {
        'form': form,
        'question': question,
        'related_questions': related_questions
    }
    return render(request, 'djora/answer_update.html', context)


# Answer Delete Confirmation
@login_required
def answer_delete(request, pk, a_pk):
    # Check if the question exists
    question = get_object_or_404(Question, pk=pk)
    related_questions = question.tags.similar_objects()[:5]
    # Check if the answer exists
    answer = get_object_or_404(Answer, pk=a_pk)
    # Check for authorized user
    if answer.author == request.user:
        context = {
            'question': question,
            'answer': answer,
            'related_questions': related_questions
        }
        # Confirm before deleting
        return render(request, 'djora/answer_delete.html', context)
    else:
        # If current user is not author then raise an error
        raise PermissionDenied


# Answer Delete
@login_required
def answer_delete_confirm(request, pk, a_pk):
    # Check if the question exists
    question = get_object_or_404(Question, pk=pk)
    # Check if the answer exists
    answer = get_object_or_404(Answer, pk=a_pk)
    # Check for authorized user
    if answer.author == request.user:
        # Delete the answer
        answer.delete()
        # Send a success message
        messages.success(request, 'Answer deleted successfully!')
        # Redirect to answer list
        return redirect(reverse('answer_list', args=(question.pk,)))
    else:
        # If current user is not author then raise an error
        raise PermissionDenied
