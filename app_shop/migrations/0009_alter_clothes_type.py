# Generated by Django 4.0.5 on 2022-07-23 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0008_alter_clothes_type_clothesreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='type',
            field=models.CharField(choices=[('Детская', 'Детская'), ('Мужская', 'Мужская'), ('Женская', 'Женская')], max_length=15, verbose_name='Тип'),
        ),
    ]