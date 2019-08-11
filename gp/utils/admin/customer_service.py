from django.contrib import admin
from django.forms import ModelForm

from gp.forms import *
from gp.models import ChoicesCustomerService
from gp.utils.admin.client import *


# class TabularClientCustomerServices(admin.TabularInline):
#     model = ModelInterClientCustomerServices
#     extra = 0

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     attrs = {'size': 15}
    #     if db_field.attname == 'interest_level':
    #         attrs = {'size': 2}
    #     kwargs['widget'] = widgets.CheckboxSelectMultiple()
    #     return super(AdminInlineCustomerServices, self).formfield_for_dbfield(db_field, **kwargs)


class ModelFormCustomerService(ModelForm):

    class Meta:
        model = ChoicesCustomerService
        exclude = ()


# class AdminCustomerService(admin.ModelAdmin):
#     inlines = [TabularClientCustomerServices]
