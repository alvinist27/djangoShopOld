from django.shortcuts import render
from django.views import View
from .models import Clothes
from .forms import RadioForm
from django.db.models import Q


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

    def post(self, request):
        form = RadioForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            if select == '2':
                clothes = Clothes.objects.filter(Q(type='Мужская') & (Q(group='Куртка') | Q(group='Пальто') | Q(group='Жилет')))[::-1]
            elif select == '3':
                clothes = Clothes.objects.filter(Q(type='Мужская') & (Q(group='Майка') | Q(group='Футболка')))[::-1]
            elif select == '4':
                clothes = Clothes.objects.filter(Q(type='Мужская') & (Q(group='Толстовка') | Q(group='Худи') | Q(group='Кофта')))[::-1]
            elif select == '5':
                clothes = Clothes.objects.filter(Q(type='Мужская') & (Q(group='Штаны') | Q(group='Брюки') | Q(group='Джинсы')))[::-1]
            elif select == '6':
                clothes = Clothes.objects.filter(Q(type='Мужская') & (Q(group='Кроссовки') | Q(group='Сапоги')))[::-1]
            else:
                clothes = Clothes.objects.filter(type='Мужская')[::-1]
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Мужская одежда', 'clothes': clothes, 'form': form})


class ClothesWomenView(View):
    def get(self, request):
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Женская')[::-1]
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Женская одежда', 'clothes': clothes, 'form': form})

    def post(self, request):
        form = RadioForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            if select == '2':
                clothes = Clothes.objects.filter(Q(type='Женская') & (Q(group='Куртка') | Q(group='Шуба') | Q(group='Пальто') | Q(group='Жилет')))[::-1]
            elif select == '3':
                clothes = Clothes.objects.filter(Q(type='Женская') & (Q(group='Майка') | Q(group='Футболка')))[::-1]
            elif select == '4':
                clothes = Clothes.objects.filter(Q(type='Женская') & (Q(group='Толстовка') | Q(group='Худи') | Q(group='Кофта')))[::-1]
            elif select == '5':
                clothes = Clothes.objects.filter(Q(type='Женская') & (Q(group='Штаны') | Q(group='Брюки') | Q(group='Джинсы')))[::-1]
            elif select == '6':
                clothes = Clothes.objects.filter(Q(type='Женская') & (Q(group='Кроссовки') | Q(group='Сапоги')))[::-1]
            else:
                clothes = Clothes.objects.filter(type='Женская')[::-1]
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Женская одежда', 'clothes': clothes, 'form': form})


class ClothesChildView(View):
    def get(self, request):
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Детская')[::-1]
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Детская одежда', 'clothes': clothes, 'form': form})

    def post(self, request):
        form = RadioForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            if select == '2':
                clothes = Clothes.objects.filter(Q(type='Детская') & (Q(group='Куртка') | Q(group='Пальто') | Q(group='Жилет')))[::-1]
            elif select == '3':
                clothes = Clothes.objects.filter(Q(type='Детская') & (Q(group='Майка') | Q(group='Футболка')))[::-1]
            elif select == '4':
                clothes = Clothes.objects.filter(Q(type='Детская') & (Q(group='Толстовка') | Q(group='Худи') | Q(group='Кофта')))[::-1]
            elif select == '5':
                clothes = Clothes.objects.filter(Q(type='Детская') & (Q(group='Штаны') | Q(group='Брюки') | Q(group='Джинсы')))[::-1]
            elif select == '6':
                clothes = Clothes.objects.filter(Q(type='Детская') & (Q(group='Кроссовки') | Q(group='Сапоги')))[::-1]
            else:
                clothes = Clothes.objects.filter(type='Детская')[::-1]
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Детская одежда', 'clothes': clothes, 'form': form})


class ClothesView(View):
    def get(self, request, id):
        item = Clothes.objects.filter(id=id)
        return render(request, 'app_shop/clothes.html', {'item': item})
