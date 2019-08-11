from django.contrib import admin
from gp.forms import *
from gp.models import InterClientActingCities


class TabularClientCities(admin.TabularInline):
    model = InterClientActingCities
    extra = 0
    raw_id_fields = ('city', )
    # autocomplete_fields = ('city', )


class AdminCity(admin.ModelAdmin):
    list_display = ('name', 'state')
    list_filter = ('state',)
    search_fields = ('name', )
    list_per_page = 15
