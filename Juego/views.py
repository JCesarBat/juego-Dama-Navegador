from django.shortcuts import render,redirect
from .Damas import *
# Create your views here.
primerB=None

def Empezar_Partida(request):
    
    diccio={'casillas':lista_botones}
   
    
    return render(request,'Juego/Templates/Juego.html',diccio)



def  Mover_R (request,boton):
    
   
    
    
    if turno.getNum()==3 :
        
       
        
        
        Mover (comer_mas.getNum(), lista_botones[boton])
        
        return redirect('Juego')
       
    
        
    if request.session['boton']!=None:
        
        var=lista_botones[request.session['boton']]
        if var.Color=='Negras':
            if var.getcassilla1()==lista_botones[boton] or var.getcassilla2()==lista_botones[boton]:
               
                Mover(var, lista_botones[boton])
            
            
           
        if var.Color=='Blancas':
            if var.getcassillaAnt1()==lista_botones[boton] or var.getcassillaAnt2()==lista_botones[boton]:
                
                Mover(var, lista_botones[boton])
        
          
        
        request.session['boton']=boton
        return redirect('Juego')
       
        
    else:
        
        request.session['boton']=boton
        return redirect('Juego')
        
        
   
    
   
            
            
            