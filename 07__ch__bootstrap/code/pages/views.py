from django.shortcuts import render


def home_page(request):
    return render(request, 'pages/index.html')


def about_page(request):
    return render(request, 'pages/about.html')


def contact_page(request):
    return render(request, 'pages/contact.html')
