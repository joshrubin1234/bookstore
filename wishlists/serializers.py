from rest_framework import serializers
from django.contrib.auth.models import User
from wishlists.models import Wishlist, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups',]

class WishlistSerializer(serializers.ModelSerializer):
    Books = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Wishlist
        fields = ['id', 'owner', 'title', 'Books']

class ListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'title', 'author']
        

