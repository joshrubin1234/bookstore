import django
from shoppingcart.serializers import ShoppingCartItemSerializer, ShoppingCartSerializer
from shoppingcart.views import ShoppingCartItemViewSet
from wishlists.apps import WishlistsConfig
from wishlists.models import Wishlist
from bookdetails.models import Book
from shoppingcart.models import ShoppingCartItem
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from shoppingcart.models import ShoppingCart, ShoppingCartItem
from ProfileManagement.models import User
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseNotFound
from wishlists.serializers import WishlistSerializer

class WishlistViewset(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    
    def create_list(request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def insert_book(self, Book):
        self.Books.add(Book)
        return Response(status=201)

@api_view(['POST', 'PATCH'])
def add_book(request):
    book_id = request.data.get('book_id')
    wishlist_id = request.data.get('wishlist_id')
    try:
        thisbook = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponseNotFound("No book with provided ID")
    try:   
        thislist = Wishlist.objects.get(id=wishlist_id)
    except Wishlist.DoesNotExist:
        return HttpResponseNotFound("No Wishlist with provided ID")
    WishlistViewset.insert_book(thislist, thisbook)
    return Response(status=201)
    
@api_view(['DELETE'])
def move_to_cart(request):
    book_id = request.data.get('book_id')
    wishlist_id = request.data.get('wishlist_id')
    try:
        thisbook = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponseNotFound("No book with provided ID")
    try:   
        thislist = Wishlist.objects.get(id=wishlist_id)
    except Wishlist.DoesNotExist:
        return HttpResponseNotFound("No Wishlist with provided ID")
    name = thislist.owner.username
    cart_owner = get_object_or_404(User, username=name)
    cart = get_object_or_404(ShoppingCart, user=cart_owner)
    book = get_object_or_404(Book, id=book_id)
    cart_item = ShoppingCartItem(quantity=1, book=book, shopping_cart=cart)
    cart_item.save()
    thislist.Books.remove(book_id)
    return Response(status=200)

@api_view(['GET'])
def get_cart_books(request):
    user = request.data.get('user')
    cart = ShoppingCart.objects.get(user=user)
    queryset = ShoppingCartItem.objects.filter(shopping_cart=cart)
    serialized_data = ShoppingCartItemSerializer(queryset, many=True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_cart(request):
    user = request.data.get('user')
    queryset = ShoppingCart.objects.filter(user=user)
    serialized_data = ShoppingCartSerializer(queryset, many=True).data
    return Response(serialized_data)
    




    



