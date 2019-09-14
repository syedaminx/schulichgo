from django.shortcuts import render
from django.db.models import Q
from courses.models import Course

def login(request):
    return render(request, "login.html")

def search(request):
    query = request.GET.get('q')
    results = Course.objects.filter(Q(code__icontains=query) | Q(title__icontains=query))

    context = {
        'results': results
    }

    return render(request, "search_result.html", context)
