from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'email', 'text')
        labels = {
            'name': '',
            'email': '',
            'text': ''
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border"})
        }
