from django.urls import path

from movies import views

urlpatterns = [
    path('', views.MoviesListView.as_view(), name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('filter/', views.FilterMovieView.as_view(), name='filter'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='list-category'),
    path('movie/<slug:slug>/', views.MovieDetailView.as_view(), name='movie'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path('actor/<str:name>/', views.ActorDetailView.as_view(), name='actor'),
]
