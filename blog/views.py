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
    context = {}
    
    post = get_object_or_404(Post, pk=pid)
    post.counted_view += 1
    post.save()
    
    try:
        next_post = Post.objects.get(id=pid + 1)
        
        if not next_post.is_published:
            next_post = None
            
    except Post.DoesNotExist:
        next_post = None
        
    try:        
        pre_post = Post.objects.get(id=pid-1)        
        
        if not pre_post.is_published:
            pre_post = None
            
    except Post.DoesNotExist:
        pre_post = None
    
    context = {'post': post,
               'next_post': next_post,
               'pre_post': pre_post}
    return render(request, 'blog/blog-single.html', context)

def test_view(request):
    return render(request, 'website/404-page.html')