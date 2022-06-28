from django.core.paginator import Paginator
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


def get_clothes_list(select, type):
    if select == '2':
        clothes = Clothes.objects.filter(
            Q(type=type) & (Q(group='Куртка') | Q(group='Пальто') | Q(group='Шуба') | Q(group='Жилет')))[::-1]
    elif select == '3':
        clothes = Clothes.objects.filter(Q(type=type) & (Q(group='Майка') | Q(group='Футболка')))[::-1]
    elif select == '4':
        clothes = Clothes.objects.filter(
            Q(type=type) & (Q(group='Толстовка') | Q(group='Худи') | Q(group='Кофта')))[::-1]
    elif select == '5':
        clothes = Clothes.objects.filter(
            Q(type=type) & (Q(group='Штаны') | Q(group='Брюки') | Q(group='Джинсы')))[::-1]
    elif select == '6':
        clothes = Clothes.objects.filter(Q(type=type) & (Q(group='Кроссовки') | Q(group='Сапоги')))[::-1]
    else:
        clothes = Clothes.objects.filter(type=type)[::-1]
    return clothes


class ClothesMenView(View):
    def get(self, request):
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Мужская')[::-1]
        paginator = Paginator(clothes, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Мужская одежда', 'clothes': page_obj, 'form': form})

    def post(self, request):
        form = RadioForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            clothes = get_clothes_list(select, 'Мужская')
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Мужская одежда', 'clothes': clothes, 'form': form})


class ClothesWomenView(View):
    def get(self, request):
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Женская')[::-1]
        paginator = Paginator(clothes, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Женская одежда', 'clothes': page_obj, 'form': form})

    def post(self, request):
        form = RadioForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            clothes = get_clothes_list(select, 'Женская')
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Женская одежда', 'clothes': clothes, 'form': form})


class ClothesChildView(View):
    def get(self, request):
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Детская')[::-1]
        paginator = Paginator(clothes, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Детская одежда', 'clothes': page_obj, 'form': form})

    def post(self, request):
        form = RadioForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            clothes = get_clothes_list(select, 'Детская')
        return render(request, 'app_shop/clothes_list.html',
                      {'name': 'Детская одежда', 'clothes': clothes, 'form': form})


class ClothesView(View):
    def get(self, request, id):
        item = Clothes.objects.filter(id=id)
        return render(request, 'app_shop/clothes.html', {'item': item})


class SearchResults(View):
    def get(self, request):
        clothes = ''
        query = self.request.GET.get('q')
        if query:
            clothes = Clothes.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        paginator = Paginator(clothes, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'app_shop/search.html', {'clothes': page_obj, 'count': paginator.count})
