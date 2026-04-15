"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from Usuario.views import UsuarioListCreate, UsuarioRetrieveUpdateDestroy
from Prefeitura.views import PrefeituraListCreate, PrefeituraRetrieveUpdateDestroy
from Secretaria.views import SecretariaListCreate, SecretariaRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),

    path('usuario/', UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('usuario/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view(), name='usuario-retrieve-update-destroy'),

    path('prefeitura/', PrefeituraListCreate.as_view(), name='prefeitura-list-create'),
    path('prefeitura/<int:pk>/', PrefeituraRetrieveUpdateDestroy.as_view(), name='prefeitura-retrieve-update-destroy'),

    path('secretaria/', SecretariaListCreate.as_view(), name='secretaria-list-create'),
    path('secretaria/<int:pk>/', SecretariaRetrieveUpdateDestroy.as_view(), name='secretaria-retrieve-update-destroy')
]

    


