import math

class cuacu :
    
    @staticmethod
    def cuadrado (x):
     return math.pow(x,2)
 
    @staticmethod
    def cubo (x):
     return math.pow(x,3)
     
x = 2
cuadrado = cuacu.cuadrado(x)
cubo = cuacu.cubo(x)

print ("El cuadrado del numero",x,"es:", int(cuadrado))
print ("El cubo del numero",x,"es:" , int(cubo))
