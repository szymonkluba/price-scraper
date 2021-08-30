from django.contrib import admin

from . import models


@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductSearchDetails)
class ProductSearchDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StoreSearchDetails)
class StoreSearchDetailsAdmin(admin.ModelAdmin):
    pass
