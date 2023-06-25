from django.db import models
from django.conf import settings
from bookdetails.models import Book
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username



class Wishlist(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.title



