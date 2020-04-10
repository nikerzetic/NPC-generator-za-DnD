from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Settlement

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'settlement/index.html'
    def get_queryset(self):
        return Settlement.objects


class DetailView(generic.DetailView):
    model = Settlement
    template_name = 'settlement/detail.html'


def edit(request):
    return HttpResponse("edit")


def save(request):
    return HttpResponse("save")
