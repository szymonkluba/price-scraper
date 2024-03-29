# Generated by Django 3.2.6 on 2021-09-01 19:48
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_alter_store_slug'),
        ('products', '0002_auto_20210830_2141'),
        ('price_lookup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsearchdetails',
            name='product',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='link', to='products.product'),
        ),
        migrations.AlterField(
            model_name='productsearchdetails',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='products_links', to='stores.store'),
        ),
        migrations.AlterField(
            model_name='storesearchdetails',
            name='store',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, related_name='search_details', to='stores.store'),
        ),
        migrations.AlterUniqueTogether(
            name='productsearchdetails',
            unique_together={('store', 'product')},
        ),
    ]
