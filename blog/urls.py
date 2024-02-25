from django.urls import path

from .views import blog_view, blog_single, test_view, categories_view, blog_search, author_view
app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('categories', categories_view, name='categories'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path('author/', author_view, name='author'),    
    path('test', test_view, name='test')
]
