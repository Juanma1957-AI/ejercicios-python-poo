#Enunciado: clase Automóvil
#Se requiere un programa que modele el concepto de un automóvil. Un automóvil tiene los siguientes atributos:
#Marca: el nombre del fabricante.
#Modelo: año de fabricación.
#Motor: volumen en litros del cilindraje del motor de un automóvil.
#Tipo de combustible: valor enumerado con los posibles valores de gasolina, bioetanol, diésel, biodiésel, gas natural.
#Tipo de automóvil: valor enumerado con los posibles valores de carro de ciudad, subcompacto, compacto, familiar, ejecutivo, SUV.
#Número de puertas: cantidad de puertas.
#Cantidad de asientos: número de asientos disponibles que tiene el vehículo.
#Velocidad máxima: velocidad máxima sostenida por el vehículo en km/h.
#Color: valor enumerado con los posibles valores de blanco, negro,  rojo, naranja, amarillo, verde, azul, violeta.
#Velocidad actual: velocidad del vehículo en un momento dado.

#La clase debe incluir los siguientes métodos:
# Un constructor para la clase Automóvil donde se le pasen como parámetros los valores de sus atributos.
# Métodos get y set para la clase Automóvil.
# Métodos para acelerar una cierta velocidad, desacelerar y frenar (colocar la velocidad actual en cero). Es importante tener en cuenta 
# que no se debe acelerar más allá de la velocidad máxima permitida para el automóvil. De igual manera, tampoco es posible 
# desacelerar a una velocidad negativa. Si se cumplen estos casos, se debe mostrar por pantalla los mensajes correspondientes.
# Un método para calcular el tiempo estimado de llegada, utilizando como parámetro la distancia a recorrer en kilómetros. El tiempo 
#estimado se calcula como el cociente entre la distancia a recorrer y la velocidad actual.
#Un método para mostrar los valores de los atributos de un Automóvil en pantalla.
# Un método main donde se deben crear un automóvil, colocar su velocidad actual en 100 km/h, aumentar su velocidad en 20 km/h, 
#luego decrementar su velocidad en 50 km/h, y después frenar. Con cada cambio de velocidad, se debe mostrar en pantalla la velocidad  actual
from enum import Enum
#ENUMS
class combustible (Enum):
    gasolina = "gasolina"
    bioetanol = "bioetanol"
    diésel = "diesel"
    biodiésel = "biodiesel"
    gas_natural = "gas natural"

class automovil(Enum):
    cuidad = "ciudad"
    subcompacto = "subcompacto"
    compacto = "compacto"
    familiar = "familiar"
    ejecutivo = "ejecutivo"
    suv = "suv"
class color (Enum):
    blanco = "blanco"
    negro = "negro"
    rojo = "rojo"
    naranja = "naranja"
    amarillo = "amarillo"
    verde = "verde"
    azul = "azul"
    violeta = "violeta"
#Clase automovil
class Automovil :
    def __init__ (self, marca , modelo , motor , tipo_combustible , tipo_automovil , numero_puertas , cantidad_asientos , velocidad_maxima , color , velocidad_actual, automatico  ):
        self.marca = marca
        self.modelo = modelo
        self.motor =  motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0
        self.automatico = automatico
        self.multas = 0
        self.valor_multa = 0
        #get
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_motor(self):
        return self.motor
    def get_tipo_combustible(self):
        return self.tipo_combustible
    def get_tipo_automovil(self):
        return self.tipo_automovil
    def get_numero_puertas(self):
        return self.numero_puertas
    def get_cantidad_asientos(self):
        return self.cantidad_asientos
    def get_velocidad_maxima(self):
        return self.velocidad_maxima
    def get_color(self):
        return self.color
    def get_velocidad_actual(self):
        return self.velocidad_actual
    def get_automatico(self):
         return self.automatico
    #set
    def set_marca(self, marca):
        self.marca = marca
    def set_modelo(self, modelo):
        self.modelo = modelo
    def set_motor(self, motor):
        self.motor = motor
    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible
    def set_tipo_automovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil
    def set_numero_puertas(self, numero_puertas):
        self.numero_puertas = numero_puertas
    def set_cantidad_asientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos
    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima
    def set_color(self, color):
        self.color = color
    def set_velocidad_actual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual
    def set_automatico(self, automatico):
        self.automatico = automatico
    def imprimir (self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} litros")
        print(f"Tipo de combustible: {self.tipo_combustible.value}")
        print(f"Tipo de automóvil: {self.tipo_automovil.value}")
        print(f"Número de puertas: {self.numero_puertas}")
        print(f"Cantidad de asientos: {self.cantidad_asientos}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.value}")
        print(f"  Velocidad actual: {self.velocidad_actual} km/h")
    def acelerar(self, incremento_velocidad):
        if self.velocidad_actual + incremento_velocidad <= self.velocidad_maxima:
          self.velocidad_actual += incremento_velocidad
        else:
         print("Ha superado la velocidad máxima. Se ha generado un multa")
        self.multas += 1
        self.valor_multa += 100
    def desacelerar(self, decremento_velocidad):
        if self.velocidad_actual - decremento_velocidad > 0:
           self.velocidad_actual -= decremento_velocidad
        else:
         print("No se puede decrementar a una velocidad negativa.")
    def tiene_multas(self):
        return self.multas > 0
    def total_multas(self):
        return self.valor_multa
        
    def frenar(self):
        "Colocar la velocidad en cero"
        self.velocidad_actual = 0
    def tiempo_estimado_llegada(self , distancia):
        "Calcular el tiempo de llegada, basado en distacia y velocidad actual"
        if self.velocidad_actual == 0:
            print("La velocidad actual es cero, no se puede calcular el tiempo estimado de llegada")
        else :
            tiempo = distancia / self.velocidad_actual
            print(f"El tiempo estimado de llegada es de {tiempo} horas")
                
if __name__ == "__main__" :
    
    marca = input("Ingrese la marca del automóvil: ")  
    modelo = int(input("Ingrese el modelo del automóvil: "))    
    motor = float(input("Ingrese el motor del automóvil (en litros): "))
    
    for com in combustible:
        print("-", com.value)
    tipo_combustible = combustible(input("Seleccione tipo de combustible: ").lower())
    
    for auto in automovil:
        print("-", auto.value)
    tipo_automovil = automovil(input("Seleccione tipo de automóvil: ").lower())
    
    numero_puertas = int(input("Ingrese el número de puertas del automóvil: "))
    cantidad_asientos = int(input("Ingrese la cantidad de asientos del automóvil: "))
    velocidad_maxima = int(input("Ingrese la velocidad máxima del automóvil (en km/h): "))
    
    for col in color:
        print("-", col.value)
    color_auto = color(input("Seleccione el color del automóvil: ").lower())
    
    automatico = input("¿Es automático? (si/no): ").lower() == "si"
    
    velocidad_actual = int(input("Ingrese la velocidad actual del automóvil (en km/h): "))  
    auto = Automovil(marca,modelo,motor,tipo_combustible,tipo_automovil,numero_puertas,cantidad_asientos,velocidad_maxima,color_auto,velocidad_actual, automatico)
    
    print(f"\n Datos del automóvil:")
    auto.imprimir()
    auto.set_velocidad_actual(100)
    print("Velocidad actual =", auto.get_velocidad_actual())

    auto.acelerar(20)
    print("Velocidad actual =", auto.get_velocidad_actual())

    auto.desacelerar(50)
    print("Velocidad actual =", auto.get_velocidad_actual())

    auto.frenar()
    print("Velocidad actual =", auto.get_velocidad_actual())
    if auto.tiene_multas():
        print("El vehículo tiene multas.")
        print("Total a pagar:", auto.total_multas())
    else:
        print("El vehículo no tiene multas.")
