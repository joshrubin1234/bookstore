from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=False,null=False, default='')
    email = models.EmailField(blank=False,null=False, default='')
    address = models.CharField(max_length=100,blank=False,null=False, default='') 

    def __str__(self):
        return self.username

class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit_cards')
    number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.number
