from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="blog-index"),
    path('create', views.create, name="blog-create"),
    path('<str:title>/read', views.read, name="blog-read"),
    path('<str:title>/update', views.update, name="blog-update"),
    path('<str:title>/delete', views.delete, name="blog-delete"),
]
