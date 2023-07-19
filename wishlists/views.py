from .models import Wishlist, Book
from shoppingcart.models import ShoppingCartItem
from ProfileManagement .models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from wishlists.serializers import WishlistSerializer, ListBookSerializer, UserSerializer

class WishlistViewset(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    
    def create_list(request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListbookItemViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = ListBookSerializer

    @api_view()
    def get_queryset(self, reqtitle):
        queryset = Book.objects.filter(title=reqtitle)
        serialized_data = ListBookSerializer(queryset, many=True).data
        return Response(serialized_data)

    def move_to_cart(request, book_id, wishlist_id):
        Book = get_object_or_404(Book, id=book_id)
        Wishlist = get_object_or_404(Wishlist, id=wishlist_id)
        request.user.wishlist.remove(Book)
        ShoppingCartItem.objects.create(Book=book, user=Wishlist.owner)


    



