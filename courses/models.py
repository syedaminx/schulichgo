from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

import datetime

class Course(models.Model):
    code = models.CharField(max_length=15)
    category = models.CharField(max_length=4)
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructors = ArrayField(models.CharField(max_length=200))
    updated_at = models.DateTimeField(auto_now=True)

class Syllabus(models.Model):
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    syllabus = models.FileField(upload_to='syllabus/')
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class Category(models.Model):
    category = models.CharField(max_length=4)
    category_title = models.CharField(max_length=200)

class Review(models.Model):
    current_year = int(datetime.datetime.now().year) #to enable user to pick up to the current year
    year_choices = range(2000, current_year + 1)
    year_choices = tuple(zip(year_choices, year_choices)) #turning into a tuple because django expects actual value and human readable form, which is same in this case

    course_code = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_code')
    usefulness_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    difficulty_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    instructor_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    instructor = models.CharField(max_length=200)
    taken_season = models.CharField(max_length=200, choices=(('Fall', 'Fall'), ('Winter', 'Winter'), ('Summer', 'Summer')))
    taken_year = models.IntegerField(choices=(year_choices))
    created_at = models.DateTimeField(auto_now=True)
    anonymous = models.BooleanField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
