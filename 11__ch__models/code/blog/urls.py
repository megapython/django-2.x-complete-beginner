from django.urls import path

from .views import home_page, post_detail, create_post


urlpatterns = [
    path('', home_page, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/create/', create_post, name='create_post')
]
