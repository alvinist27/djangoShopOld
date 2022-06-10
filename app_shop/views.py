from django.shortcuts import render
from django.views import View
from .models import Clothes


class MainView(View):
    def get(self, request):
        return render(request, 'app_shop/index.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'app_shop/about.html')


class ClothesMenView(View):
    def get(self, request):
        clothes = Clothes.objects.filter(type='Мужская')
        return render(request, 'app_shop/clothes_men.html', {'clothes': clothes})


class ClothesWomenView(View):
    def get(self, request):
        clothes = Clothes.objects.filter(type='Женская')
        return render(request, 'app_shop/clothes_women.html', {'clothes': clothes})


class ClothesChildView(View):
    def get(self, request):
        clothes = Clothes.objects.filter(type='Детская')
        return render(request, 'app_shop/clothes_child.html', {'clothes': clothes})
