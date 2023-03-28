from django import forms

from movies.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email', 'text')
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
