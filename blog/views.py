from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(is_published=True)
    context = {'posts': posts}    
    return render(request, 'blog/index.html', context)

def blog_single(request, pid: int):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def test_view(request, name):
    context = {"name": name}
    return render(request, 'blog/test.html', context)