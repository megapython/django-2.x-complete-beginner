from django.urls import path

# from .views import home_page

from .views import (
    question_list,
    question_detail
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
]
