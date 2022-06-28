from django.urls import path
from .views import AboutView, MainView, ClothesView, сlothes_men_view, сlothes_women_view, сlothes_child_view, SearchResults


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about', AboutView.as_view(), name='about'),
    path('clothes/men', сlothes_men_view, name='men'),
    path('clothes/women', сlothes_women_view, name='women'),
    path('clothes/child', сlothes_child_view, name='child'),
    path('clothes/<int:id>', ClothesView.as_view(), name='clothes'),
    path('search/', SearchResults.as_view(), name='search_results')
]
