from rest_framework import serializers
from .models import Rating, Comment

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rating', 'user', 'book']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'user', 'book']