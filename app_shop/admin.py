from django.contrib import admin
from .models import Clothes, Image


class ImagesInline(admin.TabularInline):
    fk_name = 'clothes'
    model = Image


class ClothesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline,]
    list_display = ['title', 'price', 'group', 'type']
    list_filter = ['group', 'type']
    search_fields = ['title', 'description']


admin.site.register(Clothes, ClothesAdmin)
