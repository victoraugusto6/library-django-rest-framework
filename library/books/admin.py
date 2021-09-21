from django.contrib import admin

from library.books.models import Book


@admin.register(Book)
class HospedeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_year', 'state', 'pages', 'publish_company', 'created_at', 'updated_at')
    ordering = ('title',)
