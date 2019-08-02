from django.urls import path

# from .views import home_page

from .views import (
    question_list,
    question_detail,
    question_create,
    question_update,
    question_delete,
    question_delete_confirm
)

from .views import (
    answer_list,
    answer_create,
    answer_detail,
    answer_update,
    answer_delete,
    answer_delete_confirm
)

urlpatterns = [
    # path('', home_page, name='home'),
    path('', question_list, name='home'),
    # -----------------------------------------------------------------------
    #   QUESTIONS
    # -----------------------------------------------------------------------
    # Create Question
    path('question/create/', question_create, name='question_create'),
    # Question Detail
    path('question/<int:pk>/detail/', question_detail, name='question_detail'),
    # Question Update
    path('question/<int:pk>/update/', question_update, name='question_update'),
    # Question Delete
    path('question/<int:pk>/delete/', question_delete, name='question_delete'),
    # Question Delete Confirm
    path('question/<int:pk>/delete/confirm/', question_delete_confirm, name='question_delete_confirm'),
    # -----------------------------------------------------------------------
    #   ANSWERS
    # -----------------------------------------------------------------------
    # Answers List
    path('question/<int:pk>/answers', answer_list, name='answer_list'),
    # Create Answers
    path('question/<int:pk>/answer/create', answer_create, name='answer_create'),
    # Answers Detail
    path('question/<int:pk>/answer/<int:a_pk>/detail', answer_detail, name='answer_detail'),
    # Answers Update
    path('question/<int:pk>/answer/<int:a_pk>/update', answer_update, name='answer_update'),
    # Answers Delete
    path('question/<int:pk>/answer/<int:a_pk>/delete', answer_delete, name='answer_delete'),
    # Answers Delete Confirmation
    path('question/<int:pk>/answer/<int:a_pk>/delete/confirm', answer_delete_confirm, name='answer_delete_confirm'),
]
