from django.db import models
from django.conf import settings
from bookdetails.models import Book
from django.contrib.auth.models import User

class Wishlist(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.title



