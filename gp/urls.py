from django.urls import path

from .views import ClientListView, ClientDetailSlugView

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('<str:slug>/', ClientDetailSlugView.as_view(), name='detail'),
]

# {% url 'detail' slug=Client.slug %} or {{ Client.get_absolute_url }}
