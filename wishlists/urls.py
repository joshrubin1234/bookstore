from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()
router.register(r'wishlists', views.WishlistViewset)

urlpatterns = [
    path('wishlists/add/', views.add_book),
    path('wishlists/move_to_cart/', views.move_to_cart),
    path('shoppingcarthome/', views.get_cart),
    path('mycart/', views.get_cart_books),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

