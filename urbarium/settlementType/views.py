from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Category


class IndexView(generic.ListView):
    template_name = 'settlementType/index.html'

    def get_queryset(self):
        return Category.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Category
    template_name = 'settlementType/detail.html'


def edit(request):
    return HttpResponse("edit")


def save(request):
    return HttpResponse("save")
