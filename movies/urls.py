from django.urls import path

from movies import views

urlpatterns = [
    path('', views.MoviesListView.as_view(), name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='list-category'),
    path('movie/<slug:slug>/', views.MovieDetailView.as_view(), name='movie')
]
