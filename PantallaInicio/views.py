from django.shortcuts import render,redirect
from django.http import HttpResponse
import tkinter.messagebox
# Create your views here.

def Pantalla_Inicio(request):
    
  
    return render(request,'PantallaInicio/Template/Pantalla_Inicio.html')
    
    
    
def Pantalla_Inicio_Creado(request):
    request.session['boton']=None
    return redirect('/Empezar/?Creado')

