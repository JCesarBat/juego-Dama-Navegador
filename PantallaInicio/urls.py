# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 22:59:31 2023

@author: JC
"""

from django.urls import path
from PantallaInicio import views
urlpatterns = [
    path('Empezar/',views.Pantalla_Inicio,name='Empezar'),
    path('Empezar_Info/',views.Pantalla_Inicio_Creado,name='Empezar_Info'),
]