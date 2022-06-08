from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AuthForm(AuthenticationForm):
    username = forms.CharField(max_length=80, required=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=80, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
