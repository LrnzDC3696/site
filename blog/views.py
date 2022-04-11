from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, "blog/index.html", context=context)


def detail_blog(request, id):
    context = {"id": id}
    return render(request, "blog/view_post.html", context=context)
