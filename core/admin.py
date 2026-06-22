from django.contrib import admin
from core import models


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'abbreviation']
    search_fields = ['name', 'abbreviation']
    list_filter = ['name']
    list_editable = ['name']
    ordering = ['name']
    list_per_page = 5


# Register your models here.
@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'state']
    search_fields = ['name']
    list_filter = ['name']
    list_editable = ['name']
    ordering = ['name']
    list_per_page = 5


admin.site.site_header = 'Painel de administração'


@admin.register(models.Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ['name', 'abbreviation']
    list_filter = ['name']


@admin.register(models.District)
class District(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']
