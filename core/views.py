from django.shortcuts import render
from gp.models import *
from django.views.generic import DetailView, ListView


class IndexListView(ListView):
    queryset = Client.objects.all()
    template_name = 'index.html'


def index_list_view(request):
    queryset = Client.objects.all()
    context = {
        'object': queryset
    }
    return render(request, 'index.html', context)


# class IndexDetailView(DetailView):
#     queryset = Ethnicity.objects.all()
#     template_name = 'gallery/category.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(IndexDetailView, self).get_context_data(**kwargs)
#         return context
#
#
# def index_detail_view(request):
#     instance = Ethnicity.objects.all()
#     context = {
#         'object': instance,
#     }
#     return render(request, 'gallery/category.html', context)
