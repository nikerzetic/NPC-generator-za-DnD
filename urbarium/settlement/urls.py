from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


app_name = 'settlement'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', login_required(views.EditView.as_view()), name='edit'), 
    # path('new/', views.new, name='new'),
]
