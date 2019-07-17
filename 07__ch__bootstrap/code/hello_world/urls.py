from django.contrib import admin
from django.urls import path, include  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add urls from our pages app
    path('', include('pages.urls'))  # new
]
