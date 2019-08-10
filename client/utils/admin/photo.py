from django.contrib import admin
from client.forms import *
from client.utils.admin.widgets.PictureShow import PictureShowWidget


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ('photo', 'title', 'description')
        widgets = {
            'photo': PictureShowWidget()
        }


class TabularClientPhotos(admin.TabularInline):
    model = Photo
    form = PhotoForm
    extra = 0
    # template = 'admin/tabular.html'







