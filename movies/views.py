from django.shortcuts import render
from django.views.generic import ListView

from movies.models import Movie


class MoviesListView(ListView):
    model = Movie
