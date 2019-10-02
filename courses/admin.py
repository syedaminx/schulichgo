from django.contrib import admin
from .models import Category, Course, Review, Syllabus

admin.site.register(Category)
admin.site.register(Syllabus)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'comment', 'created_at', 'instructor')
