from django.shortcuts import render
from .models import Post
# Create your views here.

def helloworld(request):
    return render(request, 'helloworld.html')

def post_list(request):
    posts=Post.objects.all()

    return render(request, 'post_list.html', {
        'posts':posts
    })