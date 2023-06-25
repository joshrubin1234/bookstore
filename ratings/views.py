from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from django.http import JsonResponse
from .serializers import RatingSerializer, CommentSerializer
from .models import Rating, Comment

class CreateRatingView(APIView):
    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)
    
class CreateCommentView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)
    
class ListCommentsView(APIView):
    def get(self, request):
        book_id = request.query_params.get('book_id')
        comments = Comment.objects.filter(book_id=book_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
class AverageRatingView(APIView):
    def get(self, request):
        book_id = request.query_params.get('book_id')
        ratings = Rating.objects.filter(book_id=book_id)
        total_ratings = len(ratings)
        if total_ratings == 0:
            return Response({'average_rating': 0.0})
        sum_ratings = sum([rating.rating for rating in ratings])
        average_rating = sum_ratings / total_ratings
        return Response({'average_rating': average_rating})