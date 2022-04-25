from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post
from utils.util import to_matrix


def index(request):
    x, y = (3, 2)

    posts = Post.objects.all()
    paginator = Paginator(posts, x*y)
    page_num = request.GET.get('blog_page', 1)
    page_obj = paginator.page(page_num)
    blog_posts = to_matrix(page_obj, 3)
    context = {'page_obj': page_obj, 'blog_posts': blog_posts}

    return render(request, 'main/index.html', context)
