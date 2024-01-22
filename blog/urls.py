from django.urls import path

from .views import blog_view, blog_single, test_view

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('test', test_view, name='test')    
]
