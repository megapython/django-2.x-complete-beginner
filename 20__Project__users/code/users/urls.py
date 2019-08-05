from django.urls import path

from .views import sign_up, profile, profile_update


urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/update/', profile_update, name='profile_update')
]
