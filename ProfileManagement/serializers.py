from rest_framework import serializers
from .models import User
from .models import CreditCard

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'email', 'address')
        read_only_fields = ('email',)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('email', None)  
        return super().update(instance, validated_data)

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('number', 'expiration_date', 'cvv')

    def create(self, validated_data):
        user = self.context['user']
        credit_card = CreditCard.objects.create(user=user, **validated_data)
        return credit_card

