from django.urls import path

# from .views import home_page

from .views import (
    question_list,
    question_detail,
    question_create,
    question_update,
)


urlpatterns = [
    # path('', home_page, name='home'),
    
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
]
