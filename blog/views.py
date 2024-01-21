from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
# import datetime
# Create your views here.

def blog_view(request):
    # posts = Post.objects.filter(is_published=True)
    
    posts = Post.objects.filter(published_date__lte=timezone.now(), is_published=True)
    context = {'posts': posts}    
    return render(request, 'blog/index.html', context)

def blog_single(request, pid: int):
    post = get_object_or_404(Post, pk=pid)
    post.counted_view += 1
    post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def test_view(request):
    return render(request, 'website/404-page.html')