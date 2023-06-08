from rest_framework import serializers
from .models import Book

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'book_descrip',
                    'price', 'author', 'genre', 'publisher',
                      'publication_yr', 'copies_sold']