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


class RadioForm(forms.Form):
    select = forms.CharField(initial='1', widget=forms.RadioSelect(choices=CHOICES))
