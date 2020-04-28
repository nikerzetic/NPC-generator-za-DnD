from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import GoverningBody


# class IndexView(generic.ListView):
#     context_object_name = 'governing_body_list'
#     template_name = 'governing-body/index.html'
#     def get_queryset(self):
#         return GoverningBody.objects.all()

# class DetailView(generic.DetailView):
#     model = GoverningBody
#     template_name = 'governing-body/detail.html'

# class EditView(generic.UpdateView):
#     model = GoverningBody
#     fields = ['name', 'classification',]
#     template_name = 'governing-body/edit.html'

# class NewView(generic.CreateView):
#     model = GoverningBody
#     fields = ['name', 'classification',]
#     template_name = 'governing-body/new.html'

def wip(request):
    return render(request, 'governing_body/index.html')
