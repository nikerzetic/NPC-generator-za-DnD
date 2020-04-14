from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Character


class IndexView(generic.ListView):
    template_name = 'character/index.html'
    context_object_name = 'character_list'
    def get_queryset(self):
        return Character.objects.order_by('id')

class DetailView(generic.DetailView):
    model = Character
    template_name = 'character/detail.html'

def edit(request):
    return HttpResponse("edit")

def save(request):
    return HttpResponse("save")

def generator(request):
    return HttpResponse("generator")

