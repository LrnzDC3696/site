from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blog-index"),
    path('<int:id>/', views.view_post, name="blog-view-slugnt"),
    path('<int:id>/<slug:slug>/', views.view_post, name="blog-view-slug"),
    path('comment/<int:id>/update/', views.update_post_comment, name="blog-comment_update"),
    path('comment/<int:id>/delete/', views.delete_post_comment, name="blog-comment_delete"),
    path('comment/<int:id>/', views.anchor_comment, name="blog-comment_anchor"),
]
