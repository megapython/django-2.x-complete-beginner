from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from ckeditor_uploader import views

# from .views import home_page

from .views import (
    question_list,
    question_detail,
    question_create,
    question_update,
    question_delete,
    question_delete_confirm,
    question_list_tags
)

from .views import (
    answer_list,
    answer_detail
)

urlpatterns = [
    # path('', home_page, name='home'),
    path('ckeditor/upload/', login_required(views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(views.browse)), name='ckeditor_browse'),
    # -----------------------------------------------------------------------
    #   QUESTIONS
    # -----------------------------------------------------------------------
    # Question List
    path('', question_list, name='home'),
    # Question Detail
    path('question/<int:pk>/detail/', question_detail, name='question_detail'),
    # Create Question
    path('question/create/', question_create, name='question_create'),
    # Question Update
    path('question/<int:pk>/update/', question_update, name='question_update'),
    # Question Delete
    path('question/<int:pk>/delete/', question_delete, name='question_delete'),
    # Question Delete Confirm
    path('question/<int:pk>/delete/confirm/', question_delete_confirm, name='question_delete_confirm'),
    # Tag
    path('tag/<slug:tag_slug>/', question_list_tags, name='question_list_with_tags'),
    # -----------------------------------------------------------------------
    #   ANSWERS
    # -----------------------------------------------------------------------
    # Answers List
    path('question/<int:pk>/answers', answer_list, name='answer_list'),
    # Answers Detail
    path('question/<int:pk>/answer/<int:a_pk>/detail', answer_detail, name='answer_detail'),
]
