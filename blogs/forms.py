from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(label="Username")
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    about = forms.CharField(label="About you")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
