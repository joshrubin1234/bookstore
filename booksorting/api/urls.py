from django.urls import path
from . import views

urlpatterns = [

    path('books', views.create_book, name='create-book'),
    path('all_books', views.get_all_books, name ='all_books'),
    path('genre/', views.books_by_genre, name ='genre'),
    path('top_sellers/', views.TopSellersView, name='top-sellers'),
    path('rating/', views.RatingView, name = 'ratings'),
    path('discount/', views.DiscountedBooks, name = 'discount'),
]

##fix genre, rating, and discount