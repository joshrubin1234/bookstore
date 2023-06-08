from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    book_descrip = models.CharField(max_length=500)
    publication_yr = models.DateField()
    publisher = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True, default='default_isbn')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    copies_sold = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title



