from django.urls import path

from .views import home_page, post_detail, create_post, post_update, post_delete, post_delete_confirm


urlpatterns = [
    path('', home_page, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/create/', create_post, name='create_post'),
    path('post/<int:pk>/update/', post_update, name='post_update'),
    path('post/<int:pk>/delete/confirm/', post_delete_confirm, name='post_delete_confirm'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
]
