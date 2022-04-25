from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blog-index"),
    path('<str:title>/', views.view_post, name="blog-view"),
]
