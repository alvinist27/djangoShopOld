from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AuthForm(AuthenticationForm):
    username = forms.CharField(max_length=80, required=True,
                               label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput,
                               label='Пароль')


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=80, required=True,
                               label='Имя пользователя')
    email = forms.EmailField(label='Email адрес')
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=8,
                                label='Введите пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=8,
                                label='Повторите пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
