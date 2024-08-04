from django.contrib import admin
from .models import Blog  # Check if the models file is in the correct location

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    def short_content(self, obj):
        # Return the first 50 characters of the content field
        return obj.content[:50]
    short_content.short_description = 'Content'  # Set the column header name
    list_display = ('title', 'author', 'short_content', 'date_created', 'image')
    list_filter = ('date_created', 'author__username')
    search_fields = ('title', 'content', 'author__username')

admin.site.register(Blog, BlogAdmin)