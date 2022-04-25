HEADER_TITLE = {
    '/': 'My Portfolio',
    '/blog/': 'My Blogs',
}


def get_header_title(request):
    return {'header_title': HEADER_TITLE.get(request.path, 'My Portfolio')}
