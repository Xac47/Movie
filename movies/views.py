from django.shortcuts import render
from django.views.generic import ListView

from movies.models import Movie


class MoviesListView(ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(draft=False).order_by('-create_at')


class CategoryListView(ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(category__url=self.kwargs.get('category')).select_related('category')