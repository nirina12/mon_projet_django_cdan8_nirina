"""
URL configuration for fiara project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homePage"),
    #path('personnes/', views.personnes, name="page_utilisateur"),
    path('actionPost/', views.actionPost, name="actionPost"),

    
    path('voitures/',views.voitures),
    
    
    
    path('personnes/ajout/', views.personnes_ajout),
    path('personne/supprimer/<int:id_personne>', views.supprimer_personne),
    path('personne/modifier/<int:id_personne>', views.modifier_personne),
    path('personne/modifier/actionPost/', views.actionPost, name="actionPost"),
]
