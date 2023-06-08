"""
URL configuration for bookdetails project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path
#from books.views import book_list
from django.http import HttpResponse
from books.views import admin_welcome
from books.views import create_books
from books.views import BookListView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url = '/static/favicon.ico')),
    #path('books/', book_list, name='book_list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('admin/', admin_welcome),
    path('create/books', create_books, name='create_books'),

]
