from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'objs': [[*page_obj[i:i+3]] for i in range(0, len(page_obj), 3)],
        'page_obj': page_obj
    }

    return render(request, "blog/index.html", context=context)


def create(request):
    context = {}

    return render(request, "blog/create_post.html", context=context)


def read(request, title):
    post = get_object_or_404(Post, title=title)
    context = {"post": post}

    return render(request, "blog/view_post.html", context=context)


def update(request, title):
    posts = get_object_or_404(Post, title=title)
    context = {"posts": posts}

    return render(request, "blog/edit_post.html", context=context)


def delete(request, title):
    posts = get_object_or_404(Post, title=title)
    context = {"posts": posts}

    return render(request, "blog/delete_post.html", context=context)
