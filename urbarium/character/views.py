from django.views import generic
from django.urls import reverse

from random import randint

from character.models import *


class IndexView(generic.ListView):
    context_object_name = 'character_list'
    template_name = 'character/index.html'
    def get_queryset(self):
        return Character.objects.all()


class DetailView(generic.DetailView):
    model = Character
    template_name = 'character/detail.html'
    # ??? dodati se titles in conections na kraje


class EditView(generic.UpdateView):
    model = Character
    template_name = 'character/edit.html'
    fields = [
        'name', 'surname', 'race', 'gender', 'age',
        'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
        'appearance', 'mannerism', 'interactionTrait', 'ideal', 'bond', 'notes',
        ]


class NewView(generic.CreateView):
    model = Character
    template_name = 'character/new.html'
    fields = [
        'name', 'surname', 'race', 'gender', 'age',
        'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
        'appearance', 'mannerism', 'interactionTrait', 'ideal', 'bond', 'notes',
        ]

class Generator(generic.CreateView):
    model = Character
    template_name = 'character/generator.html'
    fields = [
        'name', 'surname', 'race', 'gender', 'age',
        'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
        'appearance', 'mannerism', 'interactionTrait', 'ideal', 'bond', 'notes',
        ]
    def get_initial(self):
        return {
            'gender': Gender.objects.get(pk=randint(1,Gender.objects.count())),
            'race': Race.objects.get(pk=randint(1,Race.objects.count())),
            'age': randint(0,100),
            'strength': randint(6,18),
            'dexterity': randint(6,18),
            'constitution': randint(6,18),
            'intelligence': randint(6,18),
            'wisdom': randint(6,18),
            'charisma': randint(6,18), # ??? Tu bi bilo potrebno prilagditi, da je porazdelitev bolj normalna
            'appearance': Appearance.objects.get(pk=randint(1,Appearance.objects.count())),
            # 'mannerism': Mannerism.objects.get(pk=randint(1,Mannerism.objects.count())),
            # 'interactionTrait': Appearance.objects.get(pk=randint(1,Appearance.objects.count())),
            'ideal': Appearance.objects.get(pk=randint(1,Appearance.objects.count())),
            'bond': Appearance.objects.get(pk=randint(1,Appearance.objects.count())),
        }
