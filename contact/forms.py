from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from contact.models import SubscribeEmail


class SubscribeEmailForm(forms.ModelForm):
    captch = ReCaptchaField()

    class Meta:
        model = SubscribeEmail
        fields = ('email', 'captch')
        labels = {
            'email': ''
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'editContent', 'placeholder': 'Enter your email...'})
        }
