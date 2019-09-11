from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Category, Course, Review, Syllabus
from .forms import ReviewForm, SyllabusForm
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
import json
from django.core.serializers.json import DjangoJSONEncoder

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'courses/home.html', context)

def category(request, category):
    category_object = Category.objects.get(category=category)
    course_list = Course.objects.all().filter(category=category)
    context = {
        'categories': category_object,
        'courses': course_list
    }
    return render(request, 'courses/category.html', context)

def course(request, category, number):
    course_object = Course.objects.get(category=category, number=number)
    reviews = Review.objects.all().filter(course_code_id=course_object.pk).order_by('-created_at').values('usefulness_rating', 'difficulty_rating', 'instructor_rating', 'comment', 'instructor', 'taken_season', 'taken_year', 'created_at', 'anonymous', 'author')

    try:
        syllabus = Syllabus.objects.get(course_id=course_object.pk)
    except Syllabus.DoesNotExist:
        syllabus = None

    if reviews:
        usefulness_average = round(list(reviews.aggregate(Avg('usefulness_rating')).values())[0], 2)
        difficulty_average = round(list(reviews.aggregate(Avg('difficulty_rating')).values())[0], 2)
        instructor_average = round(list(reviews.aggregate(Avg('instructor_rating')).values())[0], 2)
        overall_average = round((usefulness_average + difficulty_average + instructor_average) / 3, 1)
    else:
        overall_average = 0
        usefulness_average = 0
        difficulty_average = 0
        instructor_average = 0

    reviews_json = json.dumps(list(reviews), cls=DjangoJSONEncoder)

    context = {
        'course': course_object,
        'usefulness_average': usefulness_average,
        'difficulty_average': difficulty_average,
        'instructor_average': instructor_average,
        'overall_average': overall_average,
        'reviews': reviews_json,
        'syllabus': syllabus
    }

    return render(request, 'courses/course.html', context)

def syllabus(request, id):
    course_id = Course.objects.get(pk=id)

    if request.method == "POST" and request.is_ajax():
        form = SyllabusForm(request.POST, files=request.FILES)
        if form.is_valid():
            syllabus = form.save(commit=False)
            syllabus.uploader = request.user
            syllabus.course = course_id
            syllabus.save()
            message = {'success': 'Syllabus has been successfully uploaded'}
    else:
        form = SyllabusForm()
        message = {'error': 'There was an error trying to upload the syllabus, please try again'}

    return JsonResponse(message)

@login_required
def review(request, category, number):
    course_object=Course.objects.get(category=category, number=number)

    if request.method == "POST":
        form = ReviewForm(request.POST, instructors=course_object.instructors)
        if form.is_valid():
            review = form.save(commit=False)
            review.course_code = course_object
            review.author = request.user
            review.save()
            return HttpResponse("the review has been submitted")
    else:
        form = ReviewForm(instructors=course_object.instructors)

    context = {
        'form': form,
        'course': course_object
    }

    return render(request, 'courses/review.html', context)
