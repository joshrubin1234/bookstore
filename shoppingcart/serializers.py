from rest_framework import serializers
from .models import ShoppingCart, ShoppingCartItem
from .models import Book

class ShoppingCartSerializer(serializers.ModelSerializer):
    subtotal = serializers.DecimalField(read_only=True, max_digits=5, decimal_places=2)
    
    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'subtotal']

    def get_subtotal(self, obj):
        return obj.subtotal


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ['id', 'shopping_cart', 'book', 'quantity',]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['book'] = instance.book.title
        total_price = instance.book.price * representation['quantity']
        representation['price'] = str(total_price)
        del representation['shopping_cart']
        return representation

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']
