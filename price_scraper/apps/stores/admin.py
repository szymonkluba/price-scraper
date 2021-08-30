from django.contrib import admin

from . import models


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    pass
