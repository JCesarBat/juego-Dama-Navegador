# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 03:48:23 2023

@author: JC
"""


from django.urls import path
from Juego import views
urlpatterns = [
   path('Juego/',views.Empezar_Partida,name='Juego'),
   path('Mover_R/<int:boton>',views.Mover_R,name='Mover'),
]