from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="main-index"),
    path('projects', views.projects, name="main-projects"),
    path('resume', views.resume, name="main-resume"),
    path('contact', views.contact, name="main-contact"),
    path('about', views.about, name="main-about"),
]
