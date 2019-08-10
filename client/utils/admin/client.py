from django.contrib import admin
from django.forms import widgets

from client.utils.admin.city import TabularClientCities
from client.utils.admin.photo import TabularClientPhotos
from client.utils.admin.video import TabularClientVideos
from client.utils.admin.widgets.PictureShow import PictureShowWidget


# from app_gp.utils.admin.customer_service import TabularClientCustomerServices

# weight = models.FloatField('Peso(kg)', null=True, blank=True)
#     height = models.FloatField('Altura(m)', null=True, blank=True)
#     bust = models.FloatField('Busto(cm)', null=True, blank=True)
#     waist = models.FloatField('Cintura(cm)', null=True, blank=True)
#     butt = models.FloatField('Bunda(cm)', null=True, blank=True)
class ClientAdmin(admin.ModelAdmin):
    # form = ModelFormClient
    inlines = [TabularClientCities, TabularClientPhotos, TabularClientVideos]
    # change_form_template = 'admin/change.html'
    list_display = ('name', 'last_name', 'slug', 'description', 'age', 'profile_picture', 'cacheForHours',
                    'genre', 'eye', 'ethnicity', 'weight', 'height', 'bust', 'waist', 'butt')
    list_filter = ('genre', 'eye', 'ethnicity')
    exclude = ()

    # fieldsets = (
    #     ('Perfil', {
    #         'fields': ('name', 'fake_name', 'image_profile', 'age', 'genre', 'ethnicity')
    #     }),
    #     ('Detalhes', {
    #         'fields': ('customer_services', 'places_accepted', 'payments_accepted', 'services_offered')
    #     }),
    # )

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname in ('customer_services', 'places_accepted', 'payments_accepted', 'services_offered'):
            kwargs['widget'] = widgets.CheckboxSelectMultiple()
        if db_field.attname == 'profile_picture':
            kwargs['widget'] = PictureShowWidget()

        return super(ClientAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    #
    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.attname in ('customer_services', 'places_accepted', 'payments_accepted', 'services_offered'):
    #         kwargs['widget'] = widgets.CheckboxSelectMultiple()
    #
    #     return super(ClientAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    #
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     return super(ClientAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    #
    # def formfield_for_choice_field(self, db_field, request, **kwargs):
    #     return super(ClientAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)
    #
    # def get_fields(self, request, obj=None):
    #     return super(ClientAdmin, self).get_fields(request, obj)
    #
    # def get_formsets_with_inlines(self, request, obj=None):
    #     return super(ClientAdmin, self).get_formsets_with_inlines(request, obj)
    #
    # def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
    #     return super(ClientAdmin, self).get_inline_formsets(request, formsets, inline_instances, obj)
