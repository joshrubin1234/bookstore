from rest_framework import serializers
from django.contrib.auth.models import User
from wishlists.models import Wishlist, Book
from rest_framework.renderers import JSONRenderer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups',]

class WishlistSerializer(serializers.HyperlinkedModelSerializer):

    Books = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )


    class Meta:
        model = Wishlist
        fields = ['url', 'owner', 'title', 'Books']

class ListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'title', 'author']
        

