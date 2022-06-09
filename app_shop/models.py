from django.db import models

CHOICES = {
    ('Мужская', 'Мужская'),
    ('Женская', 'Женская'),
    ('Детская', 'Детская'),
}


class Clothes(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')
    type = models.CharField(max_length=15, choices=CHOICES, verbose_name='Тип')
    group = models.CharField(max_length=50, verbose_name='Группа')
    price = models.IntegerField(verbose_name='Цена')
    size = models.CharField(max_length=10, verbose_name='Размер')
    discount = models.IntegerField(verbose_name='Скидка')


class Image(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images', verbose_name='Фото')
