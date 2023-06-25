from rest_framework import serializers
from .models import Book
from .models import Author

#author serializer has to be created to handle author models

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
#book serializer has to be created to handle book models
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

