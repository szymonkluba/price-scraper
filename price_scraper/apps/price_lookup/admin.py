from django.contrib import admin

from . import models


@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductLinks)
class ProductLinksAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StoreSelectors)
class StoreSelectorsAdmin(admin.ModelAdmin):
    pass
