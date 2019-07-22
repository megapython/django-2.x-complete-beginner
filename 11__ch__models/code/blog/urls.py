from django.urls import path

from .views import home_page, post_detail


urlpatterns = [
    path('', home_page, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail')
]
