from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/<str:category>', views.category, name='category'),
    path('courses/<str:category>/<int:number>', views.course, name='course'),
    path('courses/<str:category>/<int:number>/review', views.review, name='review'),
    path('courses/<int:id>/syllabus', views.syllabus, name='syllabus'),
]
