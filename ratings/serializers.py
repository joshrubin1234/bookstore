from django.contrib.auth.models import User
from bookdetails.models import Book
from rest_framework import serializers
from .models import Rating, Comment

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Rating
        fields = ['rating', 'user', 'book']

    def validate(self, attrs):
        user_id = attrs['user'].id
        book_id = attrs['book'].id

        # Check if the user ID exists
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid User ID")

        # Check if the book ID exists
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise serializers.ValidationError("Invalid Book ID")

        return attrs
    
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Comment
        fields = ['comment', 'user', 'book']

    def validate(self, attrs):
        user_id = attrs['user'].id
        book_id = attrs['book'].id

        # Check if the user ID exists
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid User ID")

        # Check if the book ID exists
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise serializers.ValidationError("Invalid Book ID")

        return attrs