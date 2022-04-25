from .models import Post


def get_latest_blog(request):
    blog_posts = Post.objects.all()[:2]
    return {'footer_blog_posts': blog_posts}
