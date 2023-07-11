from .models import Wishlist, Book
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from wishlists.serializers import WishlistSerializer, ListBookSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WishlistViewset(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class ListBookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = ListBookSerializer

class ListbookItemViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = ListBookSerializer

    @api_view()
    def get_queryset(self, reqtitle):
        queryset = Book.objects.filter(title=reqtitle)
        serialized_data = ListBookSerializer(queryset, many=True).data
        return Response(serialized_data)

class WishlistCreation(APIView):
    def post(self, request, username):
        owner = User.objects.get(username=username)
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    



