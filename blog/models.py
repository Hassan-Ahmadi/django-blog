from django.db import models

# Create your models here.

class Post(models.Model):
    # image
    title = models.CharField(max_length=255)
    content = models.TextField()
    # category
    # author
    counted_view = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)