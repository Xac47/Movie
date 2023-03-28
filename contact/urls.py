from django.urls import path

from contact import views

urlpatterns = [
    path('', views.SubscribeEmailView.as_view(), name='subscribe-email')
]