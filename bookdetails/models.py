from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=250)
    book_description = models.TextField(null=True)
    author = models.CharField(max_length=250)
    genre = models.CharField(max_length=255)
    publisher = models.CharField(max_length=200)
    published_yr = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_copies = models.IntegerField()

    def __str__(self):
        return self.title
