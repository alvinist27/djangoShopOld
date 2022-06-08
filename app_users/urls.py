from django.urls import path
from .views import AuthView, RegistrationView, LogoutUserView


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', AuthView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
]