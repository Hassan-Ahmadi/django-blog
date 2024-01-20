from django.urls import path

from .views import blog_view, test_view, blog_single

urlpatterns = [
    path('', blog_view, name='index'),
    path('blog/<int:pid>', blog_single, name='single'),
    # path('<int:pid>', blog_single, name='test')    
]
