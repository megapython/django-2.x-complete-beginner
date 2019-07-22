from django.urls import path

from .views import home_page, post_detail, create_post, post_update, post_delete


urlpatterns = [
    path('', home_page, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/create/', create_post, name='create_post'),
    path('post/update/<int:pk>/', post_update, name='post_update'),
    path('post/delete/<int:pk>/', post_delete, name='post_delete'),
]
