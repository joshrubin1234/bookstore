import json
from django.http import JsonResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Book
from .serializers import BookSerializer
from django.db.models import F


@api_view(['GET'])
def books_by_genre(request):
    genre = request.GET.get('genre')
    if genre is not None:
        books = Book.objects.filter(genre=genre)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=200)
    else:
        return Response({'error': 'Genre parameter is missing.'}, status=400)


@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
   

    
    # return JsonResponse(book_data, safe=False)
@api_view(['GET'])
def TopSellersView(request):
    books = Book.objects.order_by('-copies_sold')[:10]
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT','PATCH'])
def DiscountedBooks(request):
    data = request.data
    discount_percent = data.get('discount_percent')
    publisher = data.get('publisher')
    if discount_percent is not None and publisher is not None:
        Book.objects.filter(publisher=publisher).update(price=F('price') - F('price') * discount_percent / 100)
        return Response({}, status=200)
    else:
        return Response({'error': 'Discount percent or publisher parameter is missing.'}, status=400)
    
@api_view(['GET'])
def RatingView(request):
    rating = request.GET.get('rating')
    if rating is not None:
        books = Book.objects.filter(rating__gte=rating)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=200)
    else:
        return Response({'error': 'Rating parameter is missing.'}, status=400)


    