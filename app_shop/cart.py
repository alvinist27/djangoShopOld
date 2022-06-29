from decimal import Decimal
from django.conf import settings
from .models import Clothes


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, clothes, quantity=1, update_quantity=False):
        clothes_id = str(clothes.id)
        if clothes_id not in self.cart:
            self.cart[clothes_id] = {'quantity': 0,
                                     'price': str(clothes.price)}
        if update_quantity:
            self.cart[clothes_id]['quantity'] = quantity
        else:
            self.cart[clothes_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, clothes):
        clothes_id = str(clothes.id)
        if clothes_id in self.cart:
            del self.cart[clothes_id]
            self.save()

    def __iter__(self):
        clothes_ids = self.cart.keys()
        clothes = Clothes.objects.filter(id__in=clothes_ids)
        for cloth in clothes:
            self.cart[str(cloth.id)]['clothes'] = cloth

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
