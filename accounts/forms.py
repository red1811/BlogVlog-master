from django.forms import ModelForm
from django import forms


class RegisterForm(forms.Form):
    login = forms.CharField(max_length=127)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    pass1 = forms.CharField(min_length=8)
    pass2 = forms.CharField(min_length=8)
