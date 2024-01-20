from django.shortcuts import render
from .models import Post
# Create your views here.

def index_view(request):
    posts = Post.objects.filter(is_published=True)
    context = {'posts': posts}
    
    return render(request, 'blog/index.html', context)