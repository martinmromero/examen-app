"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

from django.contrib import admin
from django.urls import path
from examenes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

from examenes.views import generar_preguntas

urlpatterns += [
    path('generar/', generar_preguntas, name='generar_preguntas'),
]

from examenes.views import generar_pdf

urlpatterns += [
    path('pdf/', generar_pdf, name='generar_pdf'),
]
