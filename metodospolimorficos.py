class Profesor:
    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    def __init__(self):
        super().__init__()
        self.anios_experiencia = 0

    def imprimir(self):
        print("Es un profesor titular.")

    def mostrar_anios(self):
        print("Años =", self.anios_experiencia)


if __name__ == "__main__":
    profesor1 = ProfesorTitular()
    
    profesor1.imprimir()
    profesor1.mostrar_anios()
