from django.http import HttpResponse
from .models import Wishlist, ListBook
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from wishlists.serializers import WishlistSerializer, ListBookSerializer, UserSerializer
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WishlistViewset(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class ListBookViewset(viewsets.ModelViewSet):
    queryset = ListBook.objects.all()
    serializer_class = ListBookSerializer

class ListbookItemViewset(viewsets.ModelViewSet):
    queryset = ListBook.objects.all()
    serializer_class = ListBookSerializer

    @api_view()
    def get_queryset(reqtitle):
        queryset = ListBook.objects.filter(title=reqtitle)
        serializer_class = ListBookSerializer(queryset, many=True)
        return JsonResponse(seralizer.data)



    



