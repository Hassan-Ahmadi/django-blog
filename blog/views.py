from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
# import datetime
# Create your views here.


def blog_view(request, **kwargs):
    # posts = Post.objects.filter(is_published=True)
    posts = Post.objects.filter(published_date__lte=timezone.now(), is_published=True)

    if kwargs.get("cat_name"):
        posts = posts.filter(category__name=kwargs["cat_name"])

    if kwargs.get("author_username"):
        posts = posts.filter(author__username=kwargs["author_username"])

    if kwargs.get("tag_name") != None:
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])

    # handeling pagination
    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)

    except PageNotAnInteger:
        posts.get_page(1)

    except EmptyPage:
        posts.get_page(posts.num_pages)

    # --------------------------------

    context = {"posts": posts}
    return render(request, "blog/blogs.html", context)


def blog_single(request, pid: int):    
    context = {}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request, messages.SUCCESS, 'Successfully submitted comment. It will be published after approval.')
        else:
            messages.error(request, messages.ERROR, 'Error in form submission')
            

    posts = Post.objects.filter(
        pk=pid, is_published=True, published_date__lte=timezone.now()
    )
    post = get_object_or_404(posts)
    post.counted_view += 1
    post.save()
    comments = Comment.objects.filter(post=post.id, approved=True).order_by("-created_at")
    form = CommentForm()
    try:
        next_post = (
            Post.objects.filter(
                id__gt=post.id, is_published=True, published_date__lte=timezone.now()
            )
            .order_by("id")
            .first()
        )
        if next_post:
            if not next_post.is_published:
                next_post = None

    except Post.DoesNotExist:
        next_post = None

    try:
        pre_post = (
            Post.objects.filter(
                id__lt=post.id, is_published=True, published_date__lte=timezone.now()
            )
            .order_by("-id")
            .first()
        )

        if pre_post:
            if not pre_post.is_published:
                pre_post = None

    except Post.DoesNotExist:
        pre_post = None

    context = {"post": post, "next_post": next_post, "pre_post": pre_post, 'comments': comments, 'form': form}
    return render(request, "blog/blog-single.html", context)


def single_category_view(request, cat_name):
    posts = Post.objects.filter(is_published=True, published_date__lte=timezone.now())
    posts = posts.filter(category__name=cat_name)
    context = {"posts": posts}

    return render(request, "blog/category-single.html", context)


def categories_view(request):
    posts = Post.objects.filter(is_published=True, published_date__lte=timezone.now())
    categories = Category.objects.all()
    categories_count = {}
    for category in categories:
        counted_categ = posts.filter(category__name=category.name).count()
        if counted_categ:
            categories_count[category.name] = posts.filter(
                category__name=category.name
            ).count()

    context = {"categories": categories_count}
    return render(request, "blog/categories.html", context)


def blog_search(request):
    posts = Post.objects.filter(is_published=True, published_date__lte=timezone.now())
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)

    context = {"posts": posts}
    return render(request, "blog/blogs.html", context)


def test_view(request):
    return render(request, "blog/test.html")


def author_view(request):
    posts = Post.objects.filter(is_published=True, published_date__lte=timezone.now())
    authors = User.objects.filter(is_staff=False)
    authors_posts = {}
    for author in authors:
        authors_posts[author.username] = posts.filter(
            author__username=author.username
        ).count()

    context = {"authors": authors_posts}
    return render(request, "blog/author.html", context)


# def author_single_view(request, author_id: int):
#     print('I am called !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     posts = Post.objects.filter(is_published=True, published_date__lte=timezone.now())
#     posts = posts.filter(author__id=author_id)
#     author = User.objects.get(id=author_id)
    
#     context = {"posts": posts, "author": author}
#     return render(request, "blog/author-single.html", context)
