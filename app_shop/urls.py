from django.urls import path
from .views import AboutView, MainView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about', AboutView.as_view(), name='about'),

]