# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:47:19 2023




@author: JC
"""
# Dama 


from functools import *
#from redisenar_imagen import *
class Turno():
    def __init__(self,num):
        self.num=num
    
    def getNum(self):
        return self.num
    
    def setNum(self,num):
        self.num=num
        
        
class Comer_mas():
    def __init__(self,boton):
        self.boton=boton
    
    def getNum(self):
        return self.boton
    
    def setNum(self,boton):
        self.boton=boton
        
        

turno=Turno(1)
        
lista_botones=[]

comer_mas=Comer_mas(0)
def ComerMas(boton):
    global turno
    global comer_mas
    
       
    if (boton.getcassilla1() is not None 
        and boton.getcassilla1().getColor()is not None
        and boton.getcassilla1().getColor() != boton.getColor()
        and boton.getcassilla1().getcassilla1()is not None
        and  boton.getcassilla1().getcassilla1().getColor()== None):

           comer_mas.setNum(boton)
           
           turno.setNum(3)
           
           return
       
    if (boton.getcassilla2() is not None  
        and boton.getcassilla2().getColor()is not None 
        and boton.getcassilla2().getColor() != boton.getColor() 
        and boton.getcassilla2().getcassilla2()is not None 
        and  boton.getcassilla2().getcassilla1().getColor()== None):
        
        comer_mas.setNum(boton)
        
        turno.setNum(3)
        
        return
    
    if  (boton.getcassillaAnt1() is not None  
         and boton.getcassillaAnt1().getColor()is not None
         and boton.getcassillaAnt1().getColor() != boton.getColor() 
         and boton.getcassillaAnt1().getcassillaAnt1()is not None 
         and  boton.getcassillaAnt1().getcassillaAnt1().getColor()== None):
        
        comer_mas.setNum(boton)
       
        turno.setNum(3)
        
        return
    
    if  (boton.getcassillaAnt2() is not None  
         and boton.getcassillaAnt2().getColor()is not None
         and boton.getcassillaAnt2().getColor() != boton.getColor() 
         and boton.getcassillaAnt2().getcassillaAnt2()is not None 
         and  boton.getcassillaAnt2().getcassillaAnt2().getColor()== None):
        
        comer_mas.setNum(boton)
        
        turno.setNum(3)
        
        return
        
             
       
    
    


def ComerFicha(boton,anterior,num):
    global turno
    if anterior.getColor()=="Negras":
        
        if num==1:
            if boton.getcassilla1() is not None :
                
                if boton.getcassilla1().getColor()==None :
                   
                    var=boton.getcassilla1().getImagen()
                    
                    var2= anterior.getColor()
                    
                    boton.getcassilla1().setImagen(anterior.getImagen())
                    
                    boton.setImagen(var)
                    
                    anterior.setImagen(var)

                    boton.setColor(None)
                    
                    anterior.setColor(None)
                    
                    boton.getcassilla1().setColor(var2)
                    
                    
                   #Borrado
                    turno.setNum(1)
                    ComerMas(boton.getcassilla1())
                else :
                    pass
                   #Borrado
            else:
                return
            
        if num==2:
             
              if boton.getcassilla2() is not None :
                 
                 if boton.getcassilla2().getColor()==None :
                    
                     var=boton.getcassilla2().getImagen()
                     
                     var2= anterior.getColor()
                     
                     boton.getcassilla2().setImagen(anterior.getImagen())
                     
                     boton.setImagen(var)
                     
                     anterior.setImagen(var)

                     boton.setColor(None)
                     
                     anterior.setColor(None)
                     
                     boton.getcassilla2().setColor(var2)
                     
                     
                    #Borrado
                     turno.setNum(1)
                     ComerMas(boton.getcassilla2())
                
        else:
           return
    if anterior.getColor()=="Blancas":
        
        if num==1:
            
            
            if boton.getcassillaAnt1() is not None :
                
                if boton.getcassillaAnt1().getColor()==None :
                   
                    var=boton.getcassillaAnt1().getImagen()
                    
                    var2= anterior.getColor()
                    
                    boton.getcassillaAnt1().setImagen(anterior.getImagen())
                    
                    boton.setImagen(var)
                    
                    anterior.setImagen(var)

                    boton.setColor(None)
                    
                    anterior.setColor(None)
                    
                    boton.getcassillaAnt1().setColor(var2)
                    
                    
                    #Borrado
                    turno.setNum(2)
                    ComerMas(boton.getcassillaAnt1())
                
            else:
                
              return
            
        if num==2:
              print('este')
              
             
              if boton.getcassillaAnt2() is not None :
                 
                 if boton.getcassillaAnt2().getColor()==None :
                    
                     var=boton.getcassillaAnt2().getImagen()
                     
                     var2= anterior.getColor()
                     
                     boton.getcassillaAnt2().setImagen(anterior.getImagen())
                     
                     boton.setImagen(var)
                     
                     anterior.setImagen(var)

                     boton.setColor(None)
                     
                     anterior.setColor(None)
                     
                     boton.getcassillaAnt2().setColor(var2)
                     
                     #Borrado
                     turno.setNum(2)
                     ComerMas(boton.getcassillaAnt2())
                
        else:
                 
            return
            
def ComerFichaInv(boton,anterior,num):
    
    if anterior.getColor()=="Blancas":
        
        if num==1:
            if boton.getcassilla1() is not None :
                
                if boton.getcassilla1().getColor()==None :
                   
                    var=boton.getcassilla1().getImagen()
                    
                    var2= anterior.getColor()
                    
                    boton.getcassilla1().setImagen(anterior.getImagen())
                    
                    boton.setImagen(var)
                    
                    anterior.setImagen(var)

                    boton.setColor(None)
                    
                    anterior.setColor(None)
                    
                    boton.getcassilla1().setColor(var2)
                    
                    
                   #Borrado
                    turno.setNum(2)
                    ComerMas(boton.getcassilla1())
                
            else:
                return
            
        if num==2:
             
              if boton.getcassilla2() is not None :
                 
                 if boton.getcassilla2().getColor()==None :
                    
                     var=boton.getcassilla2().getImagen()
                     
                     var2= anterior.getColor()
                     
                     boton.getcassilla2().setImagen(anterior.getImagen())
                     
                     boton.setImagen(var)
                     
                     anterior.setImagen(var)

                     boton.setColor(None)
                     
                     anterior.setColor(None)
                     
                     boton.getcassilla2().setColor(var2)
                     
                     
                    
                     turno.setNum(2)
                     ComerMas(boton.getcassilla2())
                
        else:
            return
    if anterior.getColor()=="Negras":
        
        if num==1:
            if boton.getcassillaAnt1() is not None :
                
                if boton.getcassillaAnt1().getColor()==None :
                   
                    var=boton.getcassillaAnt1().getImagen()
                    
                    var2= anterior.getColor()
                    
                    boton.getcassillaAnt1().setImagen(anterior.getImagen())
                    
                    boton.setImagen(var)
                    
                    anterior.setImagen(var)

                    boton.setColor(None)
                    
                    anterior.setColor(None)
                    
                    boton.getcassillaAnt1().setColor(var2)
                    
                    
                    
                    #Borrado
                    turno.setNum(1)
                    
                    ComerMas(boton.getcassillaAnt1())
                
            else:
                return
            
        if num==2:
              
             
              if boton.getcassillaAnt2() is not None :
                 
                 if boton.getcassillaAnt2().getColor()==None :
                    
                     var=boton.getcassillaAnt2().getImagen()
                     
                     var2= anterior.getColor()
                     
                     boton.getcassillaAnt2().setImagen(anterior.getImagen())
                     
                     boton.setImagen(var)
                     
                     anterior.setImagen(var)

                     boton.setColor(None)
                     
                     anterior.setColor(None)
                     
                     boton.getcassillaAnt2().setColor(var2)
                     
                     
                    
                     turno.setNum(1)
                     ComerMas(boton.getcassillaAnt2())
                
        else:
            return




def Mover(boton,boton2):
    global turno
   
    
    if turno.getNum()==3:
        if boton2.getdireccionA()!=None:
            return
       
        
        if (boton.getcassilla1()==boton2 and boton.getcassilla1() is not None  
         and boton.getcassilla1().getColor()is not None
         and boton.getcassilla1().getColor() != boton.getColor() 
         and boton.getcassilla1().getcassilla1()is not None 
         and  boton.getcassilla1().getcassilla1().getColor()== None) :
            if boton.Color=='Negras' :
                ComerFicha(boton2,boton, 1)
            else  :
                ComerFichaInv(boton2, boton, 1)
                
                
        if (boton.getcassilla2()==boton2 and boton.getcassilla2() is not None  
         and boton.getcassilla2().getColor()is not None
         and boton.getcassilla2().getColor() != boton.getColor() 
         and boton.getcassilla2().getcassilla2()is not None 
         and  boton.getcassilla2().getcassilla2().getColor()== None) :
            if boton.Color=='Negras' :
                ComerFicha(boton2, boton, 2)
            else  :
                ComerFichaInv(boton2, boton, 2)  
                
        if (boton.getcassillaAnt1()==boton2 and boton.getcassillaAnt1() is not None  
         and boton.getcassillaAnt1().getColor()is not None
         and boton.getcassillaAnt1().getColor() != boton.getColor() 
         and boton.getcassillaAnt1().getcassillaAnt1()is not None 
         and  boton.getcassillaAnt1().getcassillaAnt1().getColor()== None) :
            
            if boton.Color=='Blancas' :
                ComerFicha(boton2, boton, 1)
            else  :
                ComerFichaInv(boton2, boton, 1)

        if (boton.getcassillaAnt2()==boton2 and boton.getcassillaAnt2() is not None  
         and boton.getcassillaAnt2().getColor()is not None
         and boton.getcassillaAnt2().getColor() != boton.getColor() 
         and boton.getcassillaAnt2().getcassillaAnt2()is not None 
         and  boton.getcassillaAnt2().getcassillaAnt2().getColor()== None) :
            if boton.Color=='Blancas' :
                ComerFicha(boton2, boton, 2)
            else  :
                ComerFichaInv(boton2, boton, 2) 
                
            
        
        return

    if boton.getColor()=="Negras"  :
                
        if turno.getNum()!=2:
           return

        
        if boton2.Color==None:
            Cambiar(boton2,boton)
            
        
        if boton2.Color=='Blancas' :
           
            
            if boton2.getdireccionA()=='D' :
               
                return
            
            if boton2.getdireccionA()=='I' :
               
                return
            
            if boton.getcassilla1()==boton2 :
                
                if boton.getdireccionA()=='I' :
                    ComerFicha(boton2, boton, 2)
                    return
               
                
                ComerFicha(boton2, boton, 1)
                
            else:
                
                ComerFicha(boton2, boton, 2)
              
        return
            
            
       
       
    
    if boton.getColor()=="Blancas"  :
        
        if turno.getNum()!=1:
          
            return
        
        if boton2.Color=='Negras':
            
            if boton2.getdireccionA()=='D' :
                return
            
            
            if boton2.getdireccionA()=='I' :
                return
            
            
            if boton.getcassillaAnt1()==boton2 :
                if boton.getdireccionA()=='I' :
                    ComerFicha(boton2, boton, 2)
                    return
                
                ComerFicha(boton2, boton, 1)
                
            else:
                
                ComerFicha(boton2, boton, 2)
        
        if boton2.Color==None:
            Cambiar(boton2,boton)
            
        
        return
        
       


def Cambiar(*Arg):
    global turno
    if Arg[1].getColor()=="Negras":
        turno.setNum(turno.getNum()-1)
    if Arg[1].getColor()=="Blancas":
        turno.setNum(turno.getNum()+1)
    if len(Arg)==2:
        
        
        var=Arg[0].getImagen()
        Arg[0].setImagen(Arg[1].getImagen())
        Arg[1].setImagen(var)
        Arg[0].setColor(Arg[1].getColor())
        Arg[1].setColor(None)
       
      
                                 
    else:
       
        var=Arg[0].getImagen()
        Arg[0].setImagen(Arg[1].getImagen())
        Arg[1].setImagen(var)
        Arg[0].setColor(Arg[1].getColor())
        Arg[1].setColor(None)
        
        
        
    



#clasess

class Boton():
    def __init__(self,imagen):
        self.imagen=imagen
       
        self.cassilla1=None
        self.cassilla2=None
        self.cassillaAnt1=None
        self.cassillaAnt2=None
        self.direccionA=None
       
        
        if imagen=='imagen__fichaN' :
            
            self.Color="Negras"
            
        elif imagen=='imagen__fichaB' :
            
            self.Color="Blancas"
            
        else :
            self.Color=None
            
    def getdireccionA(self):
        return self.direccionA
  
    
    def getboton(self):
        return self.boton
    
    def getcassillaAnt1(self):
        return self.cassillaAnt1
    
    
    def getcassillaAnt2(self):
        return self.cassillaAnt2
    
    
    def getImagen(self):
        return self.imagen
    
    def getcassilla1(self):
        return self.cassilla1
    
    def getcassilla2(self):
        return self.cassilla2
    
    def getColor(self):
        return self.Color
    
    def setImagen (self,var):
        self.imagen=var
        
    
    def setcassilla1 (self,var):
        self.cassilla1=var
        
    def setcassilla2 (self,var):
        self.cassilla2=var
        
    def setColor (self,var):
        self.Color=var
        
    def setcassillaAnt1 (self,var):
        self.cassillaAnt1=var
    
    def setcassillaAnt2 (self,var):
        self.cassillaAnt2=var
        
    def setdireccionA(self,var):
         self.direccionA=var
         
    def setdireccionB(self,var):
         self.direccionB=var

#botones de fichas 
# Fila 1
cassilla1=Boton('imagen__fichaN')

cassilla2=Boton('imagen__fichaN')

cassilla3=Boton('imagen__fichaN')

cassilla4=Boton('imagen__fichaN')

# Fila 2

cassilla5=Boton('imagen__fichaN')

cassilla6=Boton('imagen__fichaN')



cassilla7=Boton('imagen__fichaN')

cassilla8=Boton('imagen__fichaN')

#fila 3
cassilla9=Boton('imagen__fichaN')

cassilla10=Boton('imagen__fichaN')

cassilla11=Boton('imagen__fichaN')

cassilla12=Boton('imagen__fichaN')


# fila 4

cassilla13=Boton(None)

cassilla14=Boton(None)


cassilla15=Boton(None)
                 
cassilla16=Boton(None)


# fila 5

cassilla17=Boton(None)

cassilla18=Boton(None)

cassilla19=Boton(None)

cassilla20=Boton(None)

# fila 6

cassilla21=Boton('imagen__fichaB')

cassilla22=Boton('imagen__fichaB')

cassilla23=Boton('imagen__fichaB')


cassilla24=Boton('imagen__fichaB')

# fila 7

cassilla25=Boton('imagen__fichaB')

cassilla26=Boton('imagen__fichaB')

cassilla27=Boton('imagen__fichaB')

cassilla28=Boton('imagen__fichaB')


# fila 8

cassilla29=Boton('imagen__fichaB')

cassilla30=Boton('imagen__fichaB')

cassilla31=Boton('imagen__fichaB')

cassilla32=Boton('imagen__fichaB')
lista_botones=[]
lista_botones.append(cassilla1)
lista_botones.append(cassilla2)
lista_botones.append(cassilla3)
lista_botones.append(cassilla4)
lista_botones.append(cassilla5)
lista_botones.append(cassilla6)
lista_botones.append(cassilla7)
lista_botones.append(cassilla8)
lista_botones.append(cassilla9)
lista_botones.append(cassilla10)
lista_botones.append(cassilla11)
lista_botones.append(cassilla12)
lista_botones.append(cassilla13)
lista_botones.append(cassilla14)
lista_botones.append(cassilla15)
lista_botones.append(cassilla16)
lista_botones.append(cassilla17)
lista_botones.append(cassilla18)
lista_botones.append(cassilla19)
lista_botones.append(cassilla20)
lista_botones.append(cassilla21)
lista_botones.append(cassilla22)
lista_botones.append(cassilla23)
lista_botones.append(cassilla24)
lista_botones.append(cassilla25)
lista_botones.append(cassilla26)
lista_botones.append(cassilla27)
lista_botones.append(cassilla28)
lista_botones.append(cassilla29)
lista_botones.append(cassilla30)
lista_botones.append(cassilla31)
lista_botones.append(cassilla32)

#enlazar casillas

# fila1
cassilla1.setcassilla1(cassilla5)
cassilla1.setcassilla2(cassilla6)

cassilla2.setcassilla1(cassilla6)
cassilla2.setcassilla2(cassilla7)

cassilla3.setcassilla1(cassilla7)
cassilla3.setcassilla2(cassilla8)

cassilla4.setcassilla1(cassilla8)
cassilla4.setdireccionA("D")


#fila2
cassilla5.setcassilla1(cassilla9)
cassilla5.setcassillaAnt1(cassilla1)
cassilla5.setdireccionA("I")

cassilla6.setcassilla1(cassilla9)
cassilla6.setcassilla2(cassilla10)
cassilla6.setcassillaAnt1(cassilla1)
cassilla6.setcassillaAnt2(cassilla2)


cassilla7.setcassilla1(cassilla10)
cassilla7.setcassilla2(cassilla11)
cassilla7.setcassillaAnt1(cassilla2)
cassilla7.setcassillaAnt2(cassilla3)

cassilla8.setcassilla1(cassilla11)
cassilla8.setcassilla2(cassilla12)
cassilla8.setcassillaAnt1(cassilla3)
cassilla8.setcassillaAnt2(cassilla4)

# fila 3

cassilla9.setcassilla1(cassilla13)
cassilla9.setcassilla2(cassilla14)
cassilla9.setcassillaAnt1(cassilla5)
cassilla9.setcassillaAnt2(cassilla6)

cassilla10.setcassilla1(cassilla14)
cassilla10.setcassilla2(cassilla15)
cassilla10.setcassillaAnt1(cassilla6)
cassilla10.setcassillaAnt2(cassilla7)

cassilla11.setcassilla1(cassilla15)
cassilla11.setcassilla2(cassilla16)
cassilla11.setcassillaAnt1(cassilla7)
cassilla11.setcassillaAnt2(cassilla8)

cassilla12.setcassilla1(cassilla16)
cassilla12.setcassillaAnt1(cassilla8)
cassilla12.setdireccionA("D")



# fila4

cassilla13.setcassilla1(cassilla17)
cassilla13.setcassillaAnt1(cassilla9)
cassilla13.setdireccionA("I")



cassilla14.setcassilla1(cassilla17)
cassilla14.setcassilla2(cassilla18)
cassilla14.setcassillaAnt1(cassilla9)
cassilla14.setcassillaAnt2(cassilla10)


cassilla15.setcassilla1(cassilla18)
cassilla15.setcassilla2(cassilla19)
cassilla15.setcassillaAnt1(cassilla10)
cassilla15.setcassillaAnt2(cassilla11)


cassilla16.setcassilla1(cassilla19)
cassilla16.setcassilla2(cassilla20)
cassilla16.setcassillaAnt1(cassilla11)
cassilla16.setcassillaAnt2(cassilla12)


#Fila 5

cassilla17.setcassilla1(cassilla21)
cassilla17.setcassilla2(cassilla22)
cassilla17.setcassillaAnt1(cassilla13)
cassilla17.setcassillaAnt2(cassilla14)


cassilla18.setcassilla1(cassilla22)
cassilla18.setcassilla2(cassilla23)
cassilla18.setcassillaAnt1(cassilla14)
cassilla18.setcassillaAnt2(cassilla15)


cassilla19.setcassilla1(cassilla23)
cassilla19.setcassilla2(cassilla24)
cassilla19.setcassillaAnt1(cassilla15)
cassilla19.setcassillaAnt2(cassilla16)


cassilla20.setcassilla1(cassilla24)
cassilla20.setcassillaAnt1(cassilla16)
cassilla20.setdireccionA("D")




#  Fila 6
cassilla21.setcassilla1(cassilla25)
cassilla21.setcassillaAnt1(cassilla17)
cassilla21.setdireccionA("I")




cassilla22.setcassilla1(cassilla25)
cassilla22.setcassilla2(cassilla26)
cassilla22.setcassillaAnt1(cassilla17)
cassilla22.setcassillaAnt2(cassilla18)


cassilla23.setcassilla1(cassilla26)
cassilla23.setcassilla2(cassilla27)
cassilla23.setcassillaAnt1(cassilla18)
cassilla23.setcassillaAnt2(cassilla19)


cassilla24.setcassilla1(cassilla27)
cassilla24.setcassilla2(cassilla28)
cassilla24.setcassillaAnt1(cassilla19)
cassilla24.setcassillaAnt2(cassilla20)




# fila 7

cassilla25.setcassilla1(cassilla29)
cassilla25.setcassilla2(cassilla30)
cassilla25.setcassillaAnt1(cassilla21)
cassilla25.setcassillaAnt2(cassilla22)


cassilla26.setcassilla1(cassilla30)
cassilla26.setcassilla2(cassilla31)
cassilla26.setcassillaAnt1(cassilla22)
cassilla26.setcassillaAnt2(cassilla23)


cassilla27.setcassilla1(cassilla31)
cassilla27.setcassilla2(cassilla32)
cassilla27.setcassillaAnt1(cassilla23)
cassilla27.setcassillaAnt2(cassilla24)


cassilla28.setcassilla1(cassilla32)
cassilla28.setcassillaAnt1(cassilla24)
cassilla28.setdireccionA("D")


#fila 8

cassilla29.setcassillaAnt1(cassilla25)
cassilla29.setdireccionA("I")

cassilla30.setcassillaAnt1(cassilla25)
cassilla30.setcassillaAnt2(cassilla26)

cassilla31.setcassillaAnt1(cassilla26)
cassilla31.setcassillaAnt2(cassilla27)

cassilla32.setcassillaAnt1(cassilla27)
cassilla32.setcassillaAnt2(cassilla28)


