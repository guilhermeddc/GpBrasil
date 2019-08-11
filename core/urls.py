from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core.views import index_list_view, IndexListView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('', index_list_view),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
