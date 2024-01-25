from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# import datetime
# Create your views here.


def blog_view(request):
    # posts = Post.objects.filter(is_published=True)

    posts = Post.objects.filter(published_date__lte=timezone.now(), is_published=True)
    context = {"posts": posts}
    return render(request, "blog/blogs.html", context)


def blog_single(request, pid: int):
    context = {}
    posts = Post.objects.filter(
        pk=pid, is_published=True, published_date__lte=timezone.now()
    )
    post = get_object_or_404(posts)
    post.counted_view += 1
    post.save()

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

    context = {"post": post, "next_post": next_post, "pre_post": pre_post}
    return render(request, "blog/blog-single.html", context)


def test_view(request):
    return render(request, "website/404-page.html")
