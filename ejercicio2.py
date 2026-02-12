import math

class Sumas:

    @staticmethod
    def calsum(suma, x):
        return suma + x

    @staticmethod
    def calcx(x, y):
        return x + math.pow(y, 2)

    @staticmethod
    def caly(suma, x, y):
        return suma + (x / y)


suma = 0
x = 20
y = 40

suma = Sumas.calsum(suma, x)
x = Sumas.calcx(x, y)
suma = Sumas.caly(suma, x, y)

print(f"El valor de X es: {x}")
print(f"El valor de Y es: {y}")
print(f"El valor de la suma es: {suma}")
