from django.db import models
from django.conf import settings

class ListBook(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Wishlist(models.Model):
    list_title = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    list_books = models.ManyToManyField(ListBook)

    def __str__(self):
        return self.list_title


