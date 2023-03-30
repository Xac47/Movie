from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from movies.forms import ReviewForm
from movies.models import Movie, Actor


class MoviesListView(ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(draft=False).order_by('-create_at')


class CategoryListView(ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(
            Q(category__url=self.kwargs.get('slug')) &
            Q(draft=False)
        ).select_related('category')


class SearchView(ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(
            Q(title__icontains=self.request.GET.get('q')) &
            Q(draft=False)
        ).order_by('-create_at')


class MovieDetailView(FormMixin, DetailView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    slug_field = 'url'
    form_class = ReviewForm

    def get_success_url(self, **kwargs):
        return self.get_object().get_absolute_url()

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.movie = self.get_object()
        if self.request.POST.get('parent'):
            self.object.parent_id = int(self.request.POST.get('parent'))
        self.object.save()
        return super().form_valid(form)

class ActorDetailView(DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    context_object_name = 'actor'
    slug_field = 'name'
    slug_url_kwarg = 'name'
