from .cart import Cart
from .models import Clothes
from django.views import View
from django.db.models import Q
from .forms import RadioForm, CartAddProductForm
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST


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


def сlothes_men_view(request):
    if request.method == 'GET':
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Мужская')[::-1]
    elif request.method == 'POST':
        form = RadioForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            clothes = get_clothes_list(select, 'Мужская')
    paginator = Paginator(clothes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_shop/clothes_list.html',
                  {'name': 'Мужская одежда', 'clothes': page_obj, 'form': form})


def сlothes_women_view(request):
    if request.method == 'GET':
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Женская')[::-1]
    elif request.method == 'POST':
        form = RadioForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            clothes = get_clothes_list(select, 'Женская')
    paginator = Paginator(clothes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_shop/clothes_list.html',
                  {'name': 'Женская одежда', 'clothes': page_obj, 'form': form})


def сlothes_child_view(request):
    if request.method == 'GET':
        form = RadioForm()
        clothes = Clothes.objects.filter(type='Детская')[::-1]
    elif request.method == 'POST':
        form = RadioForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            clothes = get_clothes_list(select, 'Детская')
    paginator = Paginator(clothes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_shop/clothes_list.html',
                  {'name': 'Детская одежда', 'clothes': page_obj, 'form': form})


class ClothesView(View):
    def get(self, request, id):
        item = Clothes.objects.filter(id=id, is_available=True)
        form = CartAddProductForm()
        return render(request, 'app_shop/clothes.html', {'item': item, 'form': form})


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


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'app_shop/cart/detail.html', {'cart': cart})


@require_POST
def cart_add(request, id):
    cart = Cart(request)
    clothes = get_object_or_404(Clothes, id=id)
    form = CartAddProductForm(request.POST)
    print(clothes)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(clothes=clothes,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    else:
        cart.add(clothes=clothes,
                 quantity=1,
                 update_quantity=False)
    return redirect('cart_detail')


def cart_remove(request, id):
    cart = Cart(request)
    clothes = get_object_or_404(Clothes, id=id)
    cart.remove(clothes)
    return redirect('cart_detail')
