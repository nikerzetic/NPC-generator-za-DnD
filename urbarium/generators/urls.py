from django.urls import path

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('character/', views.CharacterIndexView.as_view(), name='character-index'), 
    # path('character/<int:pk>/', views.CharacterDetailView.as_view(), name='character-detail'), 
    # path('character/<int:pk>/edit/', views.character_edit, name='character-edit'), 
    # path('character/<int:pk>/save/', views.character_save, name='character-save'), 
    # path('character/generator/', views.character_generator, name='character-generator'), 
    # path('settlement/', views.SettlementIndexView.as_view(), name='settlement-index'), 
    # path('settlement/<int:pk>/', views.SettlementDetailView.as_view(), name='settlement-detail'), 
    # path('settlement/<int:pk>/edit/', views.settlement_edit, name='settlement-edit'), 
    # path('settlement/<int:pk>/save/', views.settlement_save, name='settlement-save'), 
    # path('political-formation/', views.PoliticalFormationIndexView.as_view(), name='political-formation-index'), 
    # path('political-formation/<int:pk>/', views.PoliticalFormationDetailView.as_view(), name='political-formation-detail'), 
    # path('political-formation/<int:pk>/edit/', views.political_formation_edit, name='political-formation-edit'), 
    # path('political-formation/<int:pk>/save/', views.political-formation_save, name='political-formation-save'), 
    # path('governing-body/', views.GoverningBodyIndexView.as_view(), name='governing-body-index'), 
    # path('governing-body/<int:pk>/', views.GoverningBodyDetailView.as_view(), name='governing-body-detail'), 
    # path('governing-body/<int:pk>/edit/', views.governing_body_edit, name='governing-body-edit'), 
    # path('governing-body/<int:pk>/save/', views.governing-body_save, name='governing-body-save'), 
    # path('title/', views.TitleIndexView.as_view(), name='title-index'), 
    # path('title/<int:pk>/', views.TitleDetailView.as_view(), name='title-detail'), 
    # path('title/<int:pk>/edit/', views.title_edit, name='title-edit'), 
    # path('title/<int:pk>/save/', views.title_save, name='title-save'), 
]