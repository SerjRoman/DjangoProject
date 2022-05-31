from django import views
from django.shortcuts import render
from .models import Book
# Create your views here.
def father(request):
    book = Book.objects.all()
    return render(request, 'appFirstApp/father.html', {'book': book})

def index(request):
    return render(request, 'appFirstApp/index.html')