from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import ShoppingCart, ShoppingCartItem
from .serializers import ShoppingCartSerializer, ShoppingCartItemSerializer
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework import status


# Create your views here.

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
    
class ShoppingCartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()
    def list(self, request):
        if request.user.is_authenticated:
            queryset = ShoppingCart.objects.filter(user=request.user)
        else:
            queryset = ShoppingCart.objects.none() 
        serializer = ShoppingCartSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ShoppingCartItemViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingCartItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users should be able to interact with their cart items

    def get_queryset(self):
        if self.request.user.is_authenticated:
            cart = ShoppingCart.objects.get(user=self.request.user)
            return ShoppingCartItem.objects.filter(shopping_cart=cart)
        return ShoppingCartItem.objects.none() 

    def perform_create(self, serializer):
        user = self.request.user
        cart, _ = ShoppingCart.objects.get_or_create(user=user)
        serializer.save(shopping_cart=cart)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


