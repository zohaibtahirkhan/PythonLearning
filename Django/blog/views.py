from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'homepage.html', context={"posts": posts})


def blog(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog-post.html', context={"post": post})


class PostListView(ListView):
    model = Post
    template_name = 'homepage.html'
    context_object_name = 'posts'
    ordering = ['-created_time']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog-post.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog-form.html'


def about(request):
    return render(request, 'about.html')


