from django.urls import path
from .views import AboutView, MainView, ClothesView, ClothesMenView, ClothesWomenView, ClothesChildView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about', AboutView.as_view(), name='about'),
    path('clothes/men', ClothesMenView.as_view(), name='men'),
    path('clothes/women', ClothesWomenView.as_view(), name='women'),
    path('clothes/child', ClothesChildView.as_view(), name='child'),
    path('clothes/<int:id>', ClothesView.as_view(), name='clothes')
]
