from django.contrib import admin

from gp.utils.admin.client import ClientAdmin
from .models import Client, ChoicesCity, ChoicesCustomerService, ChoicesEthnicity, ChoicesEyeColor, ChoicesGenre,\
    ChoicesPaymentAccepted, ChoicesPlace, ChoicesServicesOffered, ChoicesStates, InterClientActingCities, Photo, Video
from gp.utils.admin.city import *
from gp.utils.admin.customer_service import *


class InterClientActingCitiesAdmin(admin.ModelAdmin):
    # fieldsets = ('idClient.name', 'idCity.name')
    # list_display = ('city_id.name', )
    exclude = ()


# class ClientAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'slug']
#
#     class Meta:
#         model = Client

# ADMIN CHOICES
admin.site.register(Client, ClientAdmin)
admin.site.register(ChoicesGenre)
admin.site.register(ChoicesEthnicity)
admin.site.register(ChoicesCustomerService)
admin.site.register(ChoicesPlace)
admin.site.register(ChoicesPaymentAccepted)
admin.site.register(ChoicesServicesOffered)
admin.site.register(ChoicesStates)
admin.site.register(ChoicesCity, AdminCity)

# ADMIN INTERMEDIATE
admin.site.register(InterClientActingCities, InterClientActingCitiesAdmin)