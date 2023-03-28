from django import template

from contact.forms import SubscribeEmailForm

register = template.Library()

@register.simple_tag()
def get_subscribe_email_form():
    return SubscribeEmailForm()