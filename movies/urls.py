from django.urls import path

from movies import views

urlpatterns = [
    path('', views.MoviesListView.as_view(), name='home'),
    path('category/<slug:category>/', views.CategoryListView.as_view(), name='list-category'),
]
