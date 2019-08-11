from django.contrib import admin
from django.forms import ModelForm

from gp.forms import *
from gp.models import Video
from gp.utils.admin.widgets.VideoShow import VideoShowWidget


class VideoForm(ModelForm):

    class Meta:
        model = Video
        fields = ('video', )
        widgets = {
            'video': VideoShowWidget()
        }


class TabularClientVideos(admin.TabularInline):
    model = Video
    form = VideoForm
    extra = 0
