from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from contact.forms import SubscribeEmailForm
from contact.models import SubscribeEmail


class SubscribeEmailView(CreateView):
    model = SubscribeEmail
    form_class = SubscribeEmailForm

    def get_success_url(self):
        return reverse('home')
