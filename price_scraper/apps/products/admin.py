from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "category"]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]
