from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Comment
from utils.util import to_matrix


@login_required()
def delete_post_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    post_id = comment.post.id

    if request.user != comment.author:
        # NOTE: SHOW MESSAGE
        return redirect('blog-view-slugnt', id=post_id)

    if request.method == "POST":
        # NOTE: SHOW MESSAGE
        comment.delete()
        return redirect('blog-view-slugnt', id=post_id)

    context = {'title': 'Are you sure about that?', 'comment': comment}

    return render(request, 'blog/delete_post_comment.html', context=context)

@login_required()
def update_post_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment_value = comment.context
    post_id = comment.post.id

    if request.user != comment.author:
        # NOTE: SHOW MESSAGE
        return redirect('blog-view-slugnt', id=post_id)

    if request.method == "POST":
        # NOTE: SHOW MESSAGE
        comment.context = request.POST.get('context')
        comment.save()
        return redirect('blog-view-slugnt', id=post_id)

    context = {'title': 'Updating the comment I see', 'comment_value': comment_value}
    return render(request, 'blog/update_post_comment.html', context=context)

def view_post(request, id, slug=None):
    blog_post = get_object_or_404(Post, id=id)
    comments = blog_post.comments.all()

    if slug != blog_post.slug:
        # either slug is wrong or None
        return redirect(blog_post.get_absolute_url())

    if request.method == "POST":
        comment = Comment.objects.create(
            post = blog_post,
            author = request.user,
            context = request.POST.get('context'),
        )
        return redirect('blog-view-slugnt', id=id)


    context = {'id': id, 'blog_post': blog_post, 'comments': comments}
    return render(request, 'blog/view_post.html', context)

def index(request):
    x, y = (3, 10)
    posts = Post.objects.all()
    paginator = Paginator(posts, x*y)
    page_num = request.GET.get('blog_page', 1)
    page_obj = paginator.page(page_num)
    blog_posts = to_matrix(page_obj, x)
    context = {'title': 'My Blogs', 'page_obj': page_obj, 'blog_posts': blog_posts}

    return render(request, 'blog/index.html', context)
