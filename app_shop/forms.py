from django import forms
from django.utils.safestring import mark_safe

CHOICES = (
    ('1', 'Все товары'),
    ('2', 'Верхняя одежда'),
    ('3', 'Футболки'),
    ('4', 'Толстовки'),
    ('5', 'Штаны'),
    ('6', 'Аксессуары')
)

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class RadioForm(forms.Form):
    select = forms.CharField(initial='1', widget=forms.RadioSelect(choices=CHOICES))


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
