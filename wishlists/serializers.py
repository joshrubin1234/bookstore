from rest_framework import serializers
from wishlists.models import Wishlist

class WishlistSerializer(serializers.Serializer):
    user = serializers.user()
    listbooks = serializers.Books()
    listname = serializers.CharField(max_length=255)

class ListBookSerializer(serializers.Serializer):
    title = serializers.Books()

def create(self, listname):
    return Wishlists.objects.create(**listname)
