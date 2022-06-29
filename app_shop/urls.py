from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('about', views.AboutView.as_view(), name='about'),
    path('clothes/men', views.сlothes_men_view, name='men'),
    path('clothes/women', views.сlothes_women_view, name='women'),
    path('clothes/child', views.сlothes_child_view, name='child'),
    path('clothes/<int:id>', views.ClothesView.as_view(), name='clothes'),
    path('search/', views.SearchResults.as_view(), name='search_results'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('cart_add/<int:id>', views.cart_add, name='cart_detail'),
    path('cart_remove/<int:id>', views.cart_remove, name='cart_detail'),
]
