from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django_resized import ResizedImageField

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')    
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    counted_view = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    read_duration_minutes = models.DurationField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        
        
    def __str__(self):
        return self.title
    

