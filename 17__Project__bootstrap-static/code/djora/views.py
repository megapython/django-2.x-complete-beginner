from django.shortcuts import render


# Home Page
def home_page(request):
    return render(request, 'djora/index.html')
