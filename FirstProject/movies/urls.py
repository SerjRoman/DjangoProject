from django.urls import path 
from . import views

urlpatterns = [
    path('films/', views.MoviesView.as_view(), name = 'films')
]