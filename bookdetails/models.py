from django.db import models

# Create your models here. 
    
#author db created with the following parameters
class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    biography = models.TextField(null=False)
    publisher = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#book db created with the following parameters

class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=250)
    book_description = models.TextField(null=False)
    #author = models.CharField(max_length=250)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)
    publisher = models.CharField(max_length=200)
    published_yr = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_copies = models.IntegerField()

    def __str__(self):
        return self.title
