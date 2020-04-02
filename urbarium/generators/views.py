from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


def homepage(request):
    return render(request, 'generators/homepage.html')

# def CharacterIndexView(generic.ListView):
#     template_name = 'character/index.html'
#     context_object_name = 

# def CharacterDetailView(generic.DetailView):
#     model = 
#     template_name = 'character/detail.html'

# def character_edit(request):
#     return HttpResponse("character_edit")

# def character_save(request):

# def character_generator(request):
#     return HttpResponse("character_generator")


# def SettlementIndexView(generic.ListView):
#     template_name = 
#     context_object_name = 

# def SettlementDetailView(generic.DetailView):
#     model = 
#     template_name = 

# def settlement_edit(request):
#     return HttpResponse("settlement_edit")

# def settlement_save(request):


# def PoliticalFormationIndexView(generic.ListView):
#     template_name = 
#     context_object_name = 

# def PoliticalFormationDetailView(generic.DetailView):
#     model = 
#     template_name = 

# def political_formation_edit(request):
#     return HttpResponse("political_formation_edit")

# def political_formation_save(request):


# def GoverningBodyIndexView(generic.ListView):
#     template_name = 
#     context_object_name = 

# def GoverningBodyDetailView(generic.DetailView):
#     model = 
#     template_name = 

# def governing_body_edit(request):
#     return HttpResponse("governing_body_edit")

# def governing_body_save(request):


# def TitleIndexView(generic.ListView):
#     template_name = 
#     context_object_name = 

# def TitleDetailView(generic.DetailView):
#     model = 
#     template_name = 

# def title_edit(request):
#     return HttpResponse("title_edit")

# def title_save(request):
