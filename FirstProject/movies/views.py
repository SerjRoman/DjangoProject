from pickle import FALSE
from re import template
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic import ListView

from .models import Movie
from .forms import ReviewForm
# Create your views here.

class MoviesView(ListView):
    # model = Movie
    # queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"
    def get(self, request):
        movies = Movie.objects.all() 
        return render(request, "movies/movies_list.html", {"movies_list": movies})

class MovieDetailView(View):
    
    def get(self, request, slug):
        movies = Movie.objects.get(url=slug)
        print(slug)
        return render(request, "movies/movie_detail.html", {"movie": movies})
    

class AddReview(View):
    def post(self, request, slug):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=slug)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        print(id)
        return redirect("/")