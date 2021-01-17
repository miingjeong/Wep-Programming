
from django.shortcuts import render, redirect
from .models import Post
# Create your views here.



def my_page(request):
    return render(request, 'my_page.html')

def word_count(request):
    return render(request, 'word_count.html')

    return rendef(request, 'count.html',{
        'counts':counts
    })

