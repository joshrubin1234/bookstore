from django.contrib import admin

# Register your models here.
from .models import ShoppingCart, ShoppingCartItem

admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)