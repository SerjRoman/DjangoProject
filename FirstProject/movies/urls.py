from django.urls import path 
from . import views

urlpatterns = [
    path('films/', views.MoviesView.as_view(), name = 'films'),
    path('films/<slug:slug>/', views.MovieDetailView.as_view(), name="movie_detail"),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review")
]