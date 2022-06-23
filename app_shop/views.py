from django.shortcuts import render
from django.views import View
from .models import Clothes
from .forms import RadioForm


class MainView(View):
    def get(self, request):
        return render(request, 'app_shop/index.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'app_shop/about.html')


class ClothesMenView(View):
    def get(self, request):
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Мужская')[::-1]
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Мужская одежда', 'clothes': clothes, 'form': form})


class ClothesWomenView(View):
    def get(self, request):
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Женская')[::-1]
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Женская одежда', 'clothes': clothes, 'form': form})


class ClothesChildView(View):
    def get(self, request):
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Детская')[::-1]
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Детская одежда', 'clothes': clothes, 'form': form})


class ClothesView(View):
    def get(self, request, id):
        item = Clothes.objects.filter(id=id)
        return render(request, 'app_shop/clothes.html', {'item': item})
