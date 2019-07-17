# from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    # return HttpResponse('Hello World')
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'pages/index.html')
