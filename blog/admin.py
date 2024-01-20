from django.contrib import admin

# Register your models here.
from .models import Post

# Basic admin
# admin.site.register(Post)

# Customized admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title',
                    'counted_view',
                    'is_published',
                    'created_at',
                    'published_date')
    
    list_filter = ('is_published', )
    
    # -created_at means reverse order of created at and
    #  created_at means direct order of created_at
    ordering = ('-created_at',)
    
    search_fields = ('title', 'content')
