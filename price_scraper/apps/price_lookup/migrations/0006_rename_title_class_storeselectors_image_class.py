# Generated by Django 3.2.6 on 2021-09-04 16:36
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_lookup', '0005_auto_20210904_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storeselectors',
            old_name='title_class',
            new_name='image_class',
        ),
    ]
