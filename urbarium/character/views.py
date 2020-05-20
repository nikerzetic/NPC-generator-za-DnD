from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse

from random import randint

from .models import Character, Gender, Race


class IndexView(generic.ListView):
    context_object_name = 'character_list'
    template_name = 'character/index.html'
    def get_queryset(self):
        return Character.objects.all()

class DetailView(generic.DetailView):
    model = Character
    template_name = 'character/detail.html'

class EditView(generic.UpdateView):
    model = Character
    fields = ['name', 'surname', 'race', 'gender', 'age']
    template_name = 'character/edit.html'

class NewView(generic.CreateView):
    model = Character
    fields = ['name', 'surname', 'race', 'gender', 'age']
    template_name = 'character/new.html'

def generator(request):
    random_character = Character(
        gender=Gender.objects.get(pk=randint(1,Gender.objects.count())),
        race=Race.objects.get(pk=randint(1,Race.objects.count())),
        age=randint(0,100),
        )
    context = {'character': random_character}
    return render(request, 'character/generator.html', context)

def save(request):
    return HttpResponse("save")
