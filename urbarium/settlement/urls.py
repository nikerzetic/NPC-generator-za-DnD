from django.urls import path

from . import views


app_name = 'settlement'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'), 
    # path('new/', views.new, name='new'),
]
