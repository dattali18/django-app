from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': "Daniel Attali",
        "title": "blog post 1",
        "content": "blog post",
        "date_posted": "Aug 27, 2023"
    },
    {
        'author': "Daniel",
        "title": "blog post",
        "content": "blog",
        "date_posted": "Feb 2, 2024"
    }
]


def home(request):
    context = {
        'title': 'blog home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
