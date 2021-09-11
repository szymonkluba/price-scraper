from django.contrib import admin

from . import models


@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass
