"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from .views import BookListView #view that allows user to view all books within db
from .views import BookCreateView #view that will allow user to input new books
from .views import BookInfoView #view that will allow user to get all book by isbn within db
from .views import AuthorCreateView #view that will allow an admin to create a new author within db
from .views import AuthorBookView #view will allow admin to view all books assoicated with a author

app_name = 'bookdetails'


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='create_book'),
    path('books/<str:isbn>/', BookInfoView.as_view(), name='detail-book'),
    path('author/create', AuthorCreateView.as_view(), name='create_author'),
    path('author/<int:author_id>/books/', AuthorBookView.as_view(), name='author-book'),
]



