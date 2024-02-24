from django.contrib import admin

# Register your models here.
from .models import Contact, Newsletter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    # date_hierarchy = ('-created_at',)
    search_fields = ('subject', 'message', 'name')
    list_filter = ('email',)
    
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    pass
