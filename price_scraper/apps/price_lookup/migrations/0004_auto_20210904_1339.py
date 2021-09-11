# Generated by Django 3.2.6 on 2021-09-04 11:39
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_alter_store_slug'),
        ('products', '0002_auto_20210830_2141'),
        ('price_lookup', '0003_alter_productsearchdetails_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('search_url', models.URLField()),
                ('image_url', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='links', to='products.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='products_links', to='stores.store')),
            ],
            options={
                'verbose_name_plural': 'Product Links',
                'unique_together': {('store', 'product')},
            },
        ),
        migrations.RenameModel(
            old_name='StoreSearchDetails',
            new_name='StoreSelectors',
        ),
        migrations.AlterModelOptions(
            name='storeselectors',
            options={'verbose_name_plural': 'Stores Selectors'},
        ),
        migrations.DeleteModel(
            name='ProductSearchDetails',
        ),
    ]