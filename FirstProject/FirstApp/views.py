from django import views
from django.shortcuts import get_object_or_404, render
from .models import Book
from movies.models import Category
from django.http import HttpResponse
# Create your views here.
from django.views.generic.base import View
from django.views.generic import ListView

from .models import Book

# Create your views here.

  
        








def index(request):
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context
    book = Book.objects.all()
    return render(request, 'FirstApp/index.html', {'book': book})
    

def tops(request):
    book = Book.objects.all()
    return render(request, 'appFirstApp/tops.html', {'book': book})

def books(request):
    book = Book.objects.all()
    return render(request, 'appFirstApp/books.html', {'book': book})

def categories(request):
    book = Book.objects.all()
    return render(request, 'appFirstApp/categories.html', {'book': book})



def post_info(request, book_id):
    
    
    book = get_object_or_404(Book, pk=book_id)
    context = {'book':book}
    # return HttpResponse(f'<div class="MENU">{book_id}</div>')
    return render(request, 'appFirstApp/post_info.html',context)
    

    

