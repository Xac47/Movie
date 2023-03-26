from django import template

from movies.models import Movie, Category

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('movies/include/tags/last_added.html')
def last_movies():
    movie_list = Movie.objects.filter(draft=False).order_by('-create_at')[:5]
    return {'movie_list': movie_list}