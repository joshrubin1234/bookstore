from rest_framework import serializers
from ProfileManagement.models import User
from wishlists.models import Wishlist
from bookdetails.models import Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups',]

class WishlistSerializer(serializers.ModelSerializer):

    Books = serializers.SlugRelatedField(
        queryset=Book.objects.all(),
        required=False,
        many=True,
        slug_field='title'
    )
    
    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Wishlist
        fields = ['id', 'owner', 'title', 'Books']

class ListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'title', 'author']
        

