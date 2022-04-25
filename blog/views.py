from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post
from utils.util import to_matrix


def view_post(request, title):
    blog_post = get_object_or_404(Post, title=title)
    comments = blog_post.comments.all()
    context = {'title': title, 'blog_post': blog_post, 'comments': comments}

    return render(request, 'blog/view_post.html', context)

def index(request):
    x, y = (3, 10)
    posts = Post.objects.all()
    paginator = Paginator(posts, x*y)
    page_num = request.GET.get('blog_page', 1)
    page_obj = paginator.page(page_num)
    blog_posts = to_matrix(page_obj, x)
    context = {'page_obj': page_obj, 'blog_posts': blog_posts}

    return render(request, 'blog/index.html', context)
