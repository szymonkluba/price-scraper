# Generated by Django 3.2.6 on 2021-09-04 16:34
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_lookup', '0004_auto_20210904_1339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.RemoveField(
            model_name='productlinks',
            name='image_url',
        ),
    ]
