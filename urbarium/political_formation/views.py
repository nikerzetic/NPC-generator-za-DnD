from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic

from .models import PoliticalFormation


class IndexView(generic.ListView):
    template_name = 'political_formation/index.html'
    context_object_name = 'political_formation_list'
    def get_queryset(self):
        return PoliticalFormation.objects.order_by('id')


class DetailView(generic.DetailView):
    model = PoliticalFormation
    template_name = 'political_formation/detail.html'


class EditView(generic.UpdateView):
    model = PoliticalFormation
    template_name = 'political_formation/edit.html'
    fields = ['name', 'classification', 'government',
             'governing_body']


class NewView(generic.CreateView):
    model = PoliticalFormation
    template_name = 'political_formation/new.html'
    fields = [
        'name', 'classification', 'government', 'governing_body']
