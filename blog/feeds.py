from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestEntriesFeed(Feed):
    title = "blog newst posts"
    link = "/rss/feed"
    description = "best blog ever"

    def items(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

