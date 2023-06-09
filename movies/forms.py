from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from movies.models import Review, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Review
        fields = ('name', 'email', 'text', 'captcha')
        labels = {
            'name': '',
            'email': '',
            'text': ''
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border", 'rows': 6, 'cols': 10, 'id': 'contactcomment'})
        }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)