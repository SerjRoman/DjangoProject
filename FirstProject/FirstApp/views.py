from django import views
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.http import HttpResponse
# Create your views here.
from django.views.generic.base import View
from django.views.generic import ListView

from .models import Book

# Create your views here.

class BooksView(ListView):
    # model = Movie
    # queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"
    def get(self, request):
        books = Book.objects.all() 
        return render(request, 'books/books_list.html', {"books_list": books})
        
class BookDetailView(View):    
    def get(self, request, slug):
        books = Book.objects.get(url=slug)
        return render(request, "books/book_detail.html", {"book": books})









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



def post_info(request, book_id):
    
    
    book = get_object_or_404(Book, pk=book_id)
    context = {'book':book}
    # return HttpResponse(f'<div class="MENU">{book_id}</div>')
    return render(request, 'appFirstApp/post_info.html',context)
    

    

