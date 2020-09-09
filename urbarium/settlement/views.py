from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic

from .models import Settlement


class IndexView(generic.ListView):
    template_name = 'settlement/index.html'
    context_object_name = 'settlement_list'
    def get_queryset(self):
        return Settlement.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Settlement
    template_name = 'settlement/detail.html'


class EditView(generic.UpdateView):
    model = Settlement
    template_name = 'settlement/edit.html'
    fields = ['name', 'population', 'category',
             'location', 'knownfor', 'economy']


class NewView(generic.CreateView):
    model = Settlement
    template_name = 'settlement/new.html'
    fields = [
        'name', 'population', 'category', 'location', 'knownfor', 'economy']
