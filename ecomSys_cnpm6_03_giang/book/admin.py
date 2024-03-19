from django.contrib import admin
from .models import Category, Book, Author, Publisher
from .forms import BookAdminForm

class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm

    list_display = ('title', 'price', 'quantity', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_per_page = 30
    ordering = ['-created_at']
    search_fields = ['title', 'description']
    exclude = ('created_at', 'updated_at')

admin.site.register(Book, BookAdmin)


admin.site.register(Category)

admin.site.register(Author)

admin.site.register(Publisher)
