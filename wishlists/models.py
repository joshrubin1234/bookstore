from django.db import models
from django.conf import settings
from bookdetails.models import Book

class Wishlist(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null= True, on_delete=models.SET_NULL, default=0)
    Books = models.ManyToManyField(Book)

    def __str__(self):
        return self.title

    def create(self, title):
        if serializer.is_valid():
            Wishlists.objects.create(**title)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


