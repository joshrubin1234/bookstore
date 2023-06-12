from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer



# Create your views here.

#handles get request that will allow user to view all books within created database

class BookListView(APIView):
    def get(self, request): #will output all books within database
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    
class BookCreateView(APIView):
    def post(self, request): # will allow admin to add books within db
        serializer = BookSerializer(data=request.data)
        #error code/success code that postman will output if request can/cannot post within db
        if serializer.is_valid():
            serializer.save() # will save request when successful executed
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #following code will return if request encounters an error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)