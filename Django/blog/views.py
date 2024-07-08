from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'homepage.html', context={"posts": posts})


def blog(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog-post.html', context={"post": post})


def about(request):
    return render(request, 'about.html')


