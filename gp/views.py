from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Client


class ClientFeaturedListView(ListView):
    template_name = 'gallery/gallery.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Client.objects.all().featured()


class ClientFeaturedDetailView(DetailView):
    queryset = Client.objects.all().featured()
    template_name = 'gallery/featured-girl.html'

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Client.objects.featured()


class ClientListView(ListView):
    template_name = 'gallery/gallery.html'

    # def get_context_data(self, *args, object_list=None, **kwargs):
    #     context = super(ClientListView, self).get_context_data(object_list=None, **kwargs)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Client.objects.all()


def client_list_view(request):
    queryset = Client.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'gallery/gallery.html', context)


class ClientDetailSlugView(DetailView):
    queryset = Client.objects.all()
    template_name = 'gallery/girl.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Client, slug=slug, active=True)
        return instance


class ClientDetailView(DetailView):
    # queryset = Client.objects.all()
    template_name = 'gallery/girl.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ClientDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Client.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Cliente inexistente')
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Client.objects.filter(pk=pk)


def client_detail_view(request, pk=None, *args, **kwargs):
    # instance = Client.objects.get(pk=pk, featured=True)  # id
    # instance = get_object_or_404(Client, pk=pk, featured=True)
    # try:
    #     instance = Client.objects.get(id=pk)
    # except Client.DoesNotExist:
    #     print('Cliente nao existe')
    #     raise Http404('Cliente inexistente')
    # except:
    #     print('huh?')

    instance = Client.objects.get_by_id(pk)
    if instance is None:
        raise Http404('Cliente inexistente')
    # print(instance)
    # qs = Client.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404('Cliente inexistente')

    context = {
        'object': instance
    }
    return render(request, 'gallery/girl.html', context)
