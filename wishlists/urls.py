from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()
router.register(r'wishlists', views.WishlistViewset)
router.register(r'books', views.ListbookItemViewset, basename='wishlists')
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

