from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm, AuthForm
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'app_users/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email,
                                password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'app_users/register.html', {'form': form})


class AuthView(LoginView):
    template_name = 'app_users/login.html'
    form_class = AuthForm


class LogoutUserView(LogoutView):
    next_page = '/'
