# Generated by Django 3.2.6 on 2021-08-30 19:41
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(blank=True, max_length=20),
        ),
    ]