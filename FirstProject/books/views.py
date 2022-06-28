from django.shortcuts import get_object_or_404, render
from FirstApp.models import Book
from movies.models import Category
from django.http import HttpResponse
# Create your views here.
from django.views.generic.base import View
from django.views.generic import ListView

# Create your views here.
class BooksView(ListView):
    # model = Movie
    # queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"
    model = Book
    quaryset = Book.objects.all()
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context

class BookDetailView(View):    
    def get(self, request, slug):
        books = Book.objects.get(url=slug)
        return render(request, "books/book_detail.html", {"book": books})

  