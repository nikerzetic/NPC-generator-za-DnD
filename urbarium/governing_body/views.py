from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic

from .models import GoverningBody


class IndexView(generic.ListView):
    template_name = 'governing_body/index.html'
    context_object_name = 'governing_body_list'
    def get_queryset(self):
        return GoverningBody.objects.order_by('id')


class DetailView(generic.DetailView):
    model = GoverningBody
    template_name = 'governing_body/detail.html'


class EditView(generic.UpdateView):
    model = GoverningBody
    template_name = 'governing_body/edit.html'
    fields = ['name', 'classification']


class NewView(generic.CreateView):
    model = GoverningBody
    template_name = 'governing_body/new.html'
    fields = ['name', 'classification']
