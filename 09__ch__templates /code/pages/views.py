from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Home',
        'username': 'Octallium',
        'location': 'Mumbai',
        'age': 13
    }
    return render(request, 'pages/index.html', context)


def about_page(request):
    context = {
        'title': 'About'
    }
    return render(request, 'pages/about.html', context)


def contact_page(request):
    context = {
        'title': 'Contact',
        'name': 'Mega Python'
    }
    return render(request, 'pages/contact.html', context)
