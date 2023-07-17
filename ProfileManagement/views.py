from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .serializers import CreditCardSerializer
from .models import User
from .models import CreditCard

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        if User.objects.filter(username = username).exists():
            return Response({'error': 'Username already exists.'}, status = status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_details(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
def update_user(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def partial_update_user(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_credit_card(request, username):
    user = get_object_or_404(User, username=username)
    serializer = CreditCardSerializer(data=request.data, context={'user': user})
    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_user_credit_cards(request, username):
    user = User.objects.get(username=username)
    credit_cards = user.credit_cards.all()
    serializer = CreditCardSerializer(credit_cards, many=True)
    return Response(serializer.data)
