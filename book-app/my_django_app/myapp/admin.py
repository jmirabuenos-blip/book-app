from django.contrib import admin
from .models import Book

# Register the Book model with custom admin options
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Columns shown in admin list
    search_fields = ('title', 'author')  # Searchable fields
    # Removed list_filter
