# Generated by Django 3.2.6 on 2021-09-01 19:56
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210830_2141'),
        ('price_lookup', '0002_auto_20210901_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsearchdetails',
            name='product',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='links', to='products.product'),
        ),
    ]