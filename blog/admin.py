from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post, Category

# Basic admin
# admin.site.register(Post)

# Customized admin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title',
                    'author',
                    'counted_view',
                    'is_published',
                    # 'category',
                    # 'created_at',
                    'published_date')
    
    list_filter = ('is_published', 'author')
    
    # -created_at means reverse order of created at and
    #  created_at means direct order of created_at
    ordering = ('-created_at',)
    
    search_fields = ('title', 'content')
    
    summernote_fields = ('content',)

admin.site.register(Category)