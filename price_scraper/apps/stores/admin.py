from django.contrib import admin

from . import models


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ["name", "slug", "url"]
    readonly_fields = ["slug"]