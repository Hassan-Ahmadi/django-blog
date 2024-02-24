from django import template
from django.utils import timezone

from ..models import Post
from ..models import Category

register = template.Library()


@register.simple_tag
def hello(a):
    return "hello " + str(a)


@register.simple_tag
def count_posts():
    posts_count = Post.objects.filter(is_published=True).count()
    return posts_count


@register.filter
def to_lower(text: str):
    return text.lower()

# Usage: {{ some_value | to_lower }}


@register.inclusion_tag("blog/popular-posts.html")
def popular_posts():
    pop_posts = Post.objects.filter(is_published=True).order_by("-published_date")[:3]
    return {"pop_posts": pop_posts}


# @register.inclusion_tag("blog/counted-categories.html")
# def post_categories():
#     posts = Post.objects.filter(is_published=True)
#     categories = Category.objects.all()

#     counted_categories = {}

#     for cat in categories:
#         count = posts.filter(category=cat).count()
#         if count:
#             counted_categories[cat] = count

#     return {"categories": count_posts}


@register.inclusion_tag("blog/parts/search-cat.html")
def search_by_categories():
    posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()

    counted_categories = []

    for cat in categories:
        count = posts.filter(category=cat).count()
        if count:
            counted_categories.append(cat)

    return {"categories": counted_categories}

@register.inclusion_tag("blog/parts/popular-posts.html")
def latest_posts(count=3):
    latest_posts = Post.objects.filter(is_published=True, published_date__lte=timezone.now()).order_by("published_date")[:count]
    return {"latest_posts": latest_posts}