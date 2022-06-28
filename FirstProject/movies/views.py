from audioop import reverse
from pickle import FALSE
from re import template
from urllib import request
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Category, Movie
from .forms import ReviewForm
# Create your views here.

class MoviesView(ListView):
    # model = Movie
    # queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"
    model = Movie
    quaryset = Movie.objects.filter(draft=False)
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context

class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()

        return redirect("/")