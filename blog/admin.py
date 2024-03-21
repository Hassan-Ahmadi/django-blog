from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post, Category, Comment

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
                    'login_required',
                    # 'category',
                    # 'created_at',
                    'published_date')
    
    list_filter = ('is_published', 'author')
    
    # -created_at means reverse order of created at and
    #  created_at means direct order of created_at
    ordering = ('-created_at',)
    
    search_fields = ('title', 'content')
    
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'email', 'subject', 'message','approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'post')

admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)