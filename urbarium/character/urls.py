from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), 
    path('<int:pk>/edit/', views.edit, name='edit'), 
    # path('<int:pk>/save/', views.save, name='save'), 
    path('generator/', views.generator, name='generator'),
]