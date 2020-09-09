"""urbarium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from urbarium.views import home


urlpatterns = [
    path('', home, name='homepage'),
    path('character/', include('character.urls')),
    path('settlement/', include('settlement.urls')),
    path('political-formation/', include('political_formation.urls')),
    path('governing-body/', include('governing_body.urls')),
    path('title/', include('title.urls')),
    path('users/', include('users.urls')),
    
    # inbuilt views from django
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('admin/', admin.site.urls),
] + static('static/', document_root=settings.STATICFILES_DIRS[0])
