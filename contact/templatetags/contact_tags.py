from django import template

from contact.forms import SubscribeEmailForm
from contact.models import Contact

register = template.Library()

@register.simple_tag()
def get_subscribe_email_form():
    return SubscribeEmailForm()

@register.simple_tag()
def get_contacts():
    return Contact.objects.first()