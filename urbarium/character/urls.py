from django.urls import path

from . import views


app_name = 'character'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), 
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'), 
    # path('<int:pk>/save/', views.save, name='save'), 
    path('new/', views.NewView.as_view(), name='new'),
    path('generator/', views.generator, name='generator')
]