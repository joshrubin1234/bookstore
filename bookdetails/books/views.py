from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import bookSerializer
from .models import Book
from django.http import HttpResponse
from django.views.generic import ListView





# Create your views here.

class BookListView(ListView):
    template_name = 'books_list.html'
    model = Book
    context_object_name = 'books'

#def book_list(request):
 #   books = Book.objects.all()
  #  return render(request, 'books/book_list.html',
   #               {'books': books})

def admin_welcome(request):
    return HttpResponse("Hello, welcome to Geek Text Bookstore API Service!")

@api_view(['POST'])
def create_books(request):
    serializer = bookSerializer(data=request.data)
    if serializer.is_valid():
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    #try:
     #   serializer.is_valid(raise_exception=True)
      #  serializer.save()
       # return Response(status =status.HTTP_201_CREATED)
    #except ValidationError as e:
     #   return Response(e.detail, status= status.HTTP_400_BAD_REQUEST)


