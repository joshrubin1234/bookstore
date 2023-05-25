from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'shoppingcarts', views.ShoppingCartViewSet, basename='shoppingcart')
router.register(r'shoppingcartitems', views.ShoppingCartItemViewSet, basename='shoppingcartitem')
router.register(r'books', views.BookViewSet, basename='book')  # The new line

app_name = 'shoppingcart'

urlpatterns = [
    path('', include(router.urls)),
]
