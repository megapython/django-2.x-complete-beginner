from django.shortcuts import render
from djora.models import Question, Answer
from django.db.models import Q

def search(request):
    query = request.GET.get('q')
    if query:
        q_query_set = (Q(title__icontains=query))|(Q(body__icontains=query))
        a_query_set = (Q(answer__icontains=query))
        q_results = Question.objects.filter(q_query_set).distinct()
        a_results = Answer.objects.filter(a_query_set).distinct()
        context = {
            'q_results': q_results,
            'a_results': a_results
        }
    else:
        context = {}
    return render(request, 'search.html', context)