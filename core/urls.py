from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth', include('social_django.urls', namespace='social')),
    path('results/', views.search, name='search'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service', views.terms, name='terms'),
    path('canvas-syllabus-tutorial', views.syllabus_tutorial, name='syllabus_tutorial'),
    path('resources', views.resources, name='resources')
]
