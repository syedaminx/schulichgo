from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from courses.models import Course
from courses.views import home
from .forms import FeedbackForm

def login(request):
    return render(request, "login.html")

def search(request):
    query = request.GET.get('q')

    if query:
        results = Course.objects.filter(Q(code__icontains=query) | Q(title__icontains=query))
    else:
        return redirect(home)

    context = {
        'results': results,
        'query': query
    }

    return render(request, "search_result.html", context)

def privacy_policy(request):
    return render(request, "privacy_policy.html")

def terms(request):
    return render(request, "terms.html")

def syllabus_tutorial(request):
    return render(request, "canvas_tutorial.html")

def resources(request):
    return render(request, "resources.html")

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            user = request.user
            if user != "AnonymousUser":
                feedback.author = user            
            feedback.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, "feedback.html", {'form': form})
