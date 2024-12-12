"""
URL configuration for task_manager_web project.

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
from django.contrib import admin
from django.urls import path, include

'''
importamos de django.urls el modulo include, que permite agregar paths a la definición
principal de la app utilizando paths definidos en otros lugares o apps

    * path('', include('base.urls')), ->indica que tomara en cuenta los paths definidos en base.urls
    
Entonces cuando llegue un llamado a esta url la app verificara si esta definido aqui o en base.urls.py
para definir una respuesta
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
