from django.db import models
from django.conf import settings
from django.db.models import Sum, F
from ProfileManagement.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

class ShoppingCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    @property
    def subtotal(self):
        return self.shoppingcartitem_set.aggregate(
            subtotal=Sum(F('book__price') * F('quantity'), output_field=models.DecimalField())
        )['subtotal'] or 0

class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)




# Create your models here.
