from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'title'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', login_required(views.EditView.as_view()), name='edit'), 
    path('new/', login_required(views.NewView.as_view()), name='new')
]
