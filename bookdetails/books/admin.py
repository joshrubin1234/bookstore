from django.contrib import admin
from .models import Book


# Register your models here.

@admin.register(Book)

class bookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'book_descrip',
                    'price', 'author', 'genre', 'publisher',
                      'publication_yr', 'copies_sold')