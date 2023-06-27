from django.db import models
from django.contrib.auth.models import User
from bookdetails.models import Book

# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')))
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.rating} for {self.book.title} by {self.user.username}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.book.title}"