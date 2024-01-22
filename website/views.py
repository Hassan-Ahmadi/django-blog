from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from blog.models import Post
from django.utils import timezone

# Create your views here.
# custom 404 view
def custom_404(request, exception):
    return render(request, 'website/404-page.html', status=404)

def about_view(request):
    User = get_user_model()
    users = User.objects.filter(is_superuser=False)    
    context = {'users': users}
    
    return render(request, 'website/about.html', context)

def contact_us_view(request):
    context = {'phone': '+98 919 1200 824',
               'email': 'h20.ahmadi@gmail.com',
               }
    return render(request, 'website/contact.html', context)

def index_view(request):
    
    # get last 4 posts with most views
    posts = Post.objects.filter(published_date__lte=timezone.now(), is_published=True).order_by('-counted_view')[:4]
    
    context = {'posts': posts}
    return render(request, 'website/index.html', context)