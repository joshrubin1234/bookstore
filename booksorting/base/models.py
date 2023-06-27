from django.db import models




class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    copies_sold = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    publisher = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.title
# Create your models here.
