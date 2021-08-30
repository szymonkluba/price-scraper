# Generated by Django 3.2.6 on 2021-08-30 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreSearchDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_class', models.CharField(max_length=50)),
                ('price_class', models.CharField(max_length=50)),
                ('available_class', models.CharField(max_length=50)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_search', to='stores.store')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSearchDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_url', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_search', to='products.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_details', to='stores.store')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('available', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_prices', to='products.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_prices', to='stores.store')),
            ],
        ),
    ]
