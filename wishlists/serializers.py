from rest_framework import serializers
from django.contrib.auth.models import User
from wishlists.models import Wishlist, ListBook
from rest_framework.renderers import JSONRenderer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['url', 'owner', 'title', 'listbooks']

class ListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListBook
        fields = ['url', 'title', 'author']
        

