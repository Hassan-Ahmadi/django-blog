from django.contrib import admin

# Register your models here.
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('subject', 'message')
    