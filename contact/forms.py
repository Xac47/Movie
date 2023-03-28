from django import forms

from contact.models import SubscribeEmail


class EmailForm(forms.ModelForm):
    class Meta:
        model = SubscribeEmail
        fields = ('email',)
        labels = {
            'email': ''
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'editContent', 'placeholder': 'Enter your email...'})
        }
