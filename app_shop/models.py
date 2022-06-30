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
    is_available = models.BooleanField(verbose_name='В наличии', default=True)

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'

    def __str__(self):
        return f'{self.id}'


class Image(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='images', verbose_name='Фото')


class Order(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    post_index = models.CharField(max_length=10, verbose_name='Индекс')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачен')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.id}'

    def get_total_cost(self):
        return sum(cloth.get_cost() for cloth in self.clothes.all())


class OrderCloth(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='clothes', verbose_name='Заказ')
    cloth = models.ForeignKey(Clothes, on_delete=models.CASCADE, related_name='order_items', verbose_name='Одежда')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return (self.price - self.discount) * self.quantity
