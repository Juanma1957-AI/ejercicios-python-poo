import math 
class calcular :
    @staticmethod
    def area (radio):
      return math.pi * math.pow(radio,2)
    @staticmethod
    def longitud (radio):
      return 2 * math.pi * radio

radio = 3
area = calcular.area(radio)
longitud = calcular.longitud(radio)

print(f"El área es: {area:.2f}")
print(f"La longitud es: {longitud:.2f}")
