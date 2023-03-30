from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from movies.forms import ReviewForm, RatingForm
from movies.models import Movie, Actor, Genre, Rating


class GenreYear:

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MoviesListView(GenreYear, ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(draft=False).order_by('-create_at')


class CategoryListView(GenreYear, ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(
            Q(category__url=self.kwargs.get('slug')) &
            Q(draft=False)
        ).select_related('category').order_by('-create_at')


class SearchView(GenreYear, ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(
            Q(title__icontains=self.request.GET.get('q')) &
            Q(draft=False)
        ).order_by('-create_at')


class FilterMovieView(GenreYear, ListView):

    def get_queryset(self):
        return Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        )


class MovieDetailView(FormMixin, GenreYear, DetailView):
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


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['star_form'] = RatingForm()
        return ctx


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    context_object_name = 'actor'
    slug_field = 'name'
    slug_url_kwarg = 'name'



class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)