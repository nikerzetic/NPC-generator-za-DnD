from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic

from .models import Title


class IndexView(generic.ListView):
    template_name = 'title/index.html'
    context_object_name = 'title_list'
    def get_queryset(self):
        return Title.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Title
    template_name = 'title/detail.html'


class EditView(generic.UpdateView):
    model = Title
    template_name = 'title/edit.html'
    fields = ['name', 'concerning', 'holders']


def save(request):
    return HttpResponse("save")
