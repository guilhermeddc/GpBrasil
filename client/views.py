from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *


class ClientListView(ListView):
    queryset = Client.objects.all()
    template_name = 'gallery/gallery.html'


def client_list_view(request):
    queryset = Client.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'gallery/gallery.html', context)


class CategoryDetailView(DetailView):
    queryset = Ethnicity.objects.all()
    template_name = 'gallery/category.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        return context


def category_detail_view(request, slug=None):
    instance = Ethnicity.objects.filter(ethnicity=slug)
    context = {
        'object': instance,
    }
    return render(request, 'gallery/category.html', context)


class ClientDetailView(DetailView):
    queryset = Client.objects.all()
    template_name = 'gallery/girl.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(client=self.kwargs['pk'])
        context['video'] = Video.objects.filter(client=self.kwargs['pk'])
        context['customerService'] = ChoicesCustomerService.objects.filter(client=self.kwargs['pk'])
        context['places'] = ChoicesPlace.objects.filter(client=self.kwargs['pk'])
        context['payments'] = ChoicesPaymentAccepted.objects.filter(client=self.kwargs['pk'])
        context['services'] = ChoicesServicesOffered.objects.filter(client=self.kwargs['pk'])
        return context


def client_detail_view(request, pk=None):
    qs = Client.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Client doesn't exist")

    context = {
        'object': instance
    }
    return render(request, 'gallery/girl.html', context)


# class ClientList(DetailView):
#
#     template_name = 'gallery/client_photos.html'
#     queryset = Client.objects.none()
#
#     # def get_queryset(self):
#     #     self.photos = get_object_or_404(Photo, name=self.kwargs['pk'])
#     #     return Photo.objects.filter(publisher=self.photos)
#
#     def get_context_data(self, **kwargs):
#         context = super(ClientList, self).get_context_data(**kwargs)
#         context['photos'] = Photo.objects.filter(client=self.kwargs['pk'])
#         return context

