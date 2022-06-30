from django.contrib import admin
from .models import Clothes, Image, Order, OrderCloth


class ImagesInline(admin.TabularInline):
    fk_name = 'clothes'
    model = Image


class OrderClothInline(admin.TabularInline):
    fk_name = 'order'
    model = OrderCloth


class ClothesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline,]
    list_display = ['title', 'price', 'group', 'type']
    list_filter = ['group', 'type']
    search_fields = ['title', 'description']


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderClothInline,]
    list_filter = ['is_paid', 'created', 'updated']
    list_display = ['id', 'email']


admin.site.register(Clothes, ClothesAdmin)
admin.site.register(Order, OrderAdmin)
