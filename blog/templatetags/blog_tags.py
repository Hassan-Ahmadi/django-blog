from django import template
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


@register.inclusion_tag("blog/popular-posts.html")
def popular_posts():
    pop_posts = Post.objects.filter(is_published=True).order_by("-published_date")[:3]
    return {"pop_posts": pop_posts}


@register.inclusion_tag("blog/counted-categories.html")
def post_categories():
    posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()

    counted_categories = {}

    for cat in categories:
        count = posts.filter(category=cat).count()
        if count:
            counted_categories[cat] = count

    return {"categories": count_posts}
