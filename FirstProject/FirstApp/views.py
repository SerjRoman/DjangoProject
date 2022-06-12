from django import views
from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request):
    book = Book.objects.all()
    return render(request, 'appFirstApp/index.html', {'book': book})

def tops(request):
    book = Book.objects.all()
    return render(request, 'appFirstApp/tops.html', {'book': book})

def books(request):
    book = Book.objects.all()
    return render(request, 'appFirstApp/books.html', {'book': book})

def categories(request):
    book = Book.objects.all()
    return render(request, 'appFirstApp/categories.html', {'book': book})
