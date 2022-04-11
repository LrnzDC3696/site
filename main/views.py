from django.shortcuts import render, redirect
# from django.views import View

def about(request):
    return render(request, 'main/about.html')

# does not exists
def blog(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def index(_):
    return redirect(about)

# Create your views here.
def projects(request):
    return render(request, 'main/projects.html')

# does not exists
def resume(request):
    return render(request, 'main/index.html')
