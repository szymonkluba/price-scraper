from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'category', 'image_url']
    readonly_fields = ['slug']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    readonly_fields = ['slug']
