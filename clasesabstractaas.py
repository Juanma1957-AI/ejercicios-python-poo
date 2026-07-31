from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass


class Canido(Animal):
    pass


class Felino(Animal):
    pass


class Perro(Canido):

    def get_sonido(self):
        return "Ladrido"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Doméstico"

    def get_nombre_cientifico(self):
        return "Canis lupus familiaris"


class Lobo(Canido):

    def get_sonido(self):
        return "Aullido"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Bosque"

    def get_nombre_cientifico(self):
        return "Canis lupus"


class Leon(Felino):

    def get_sonido(self):
        return "Rugido"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Praderas"

    def get_nombre_cientifico(self):
        return "Panthera leo"


class Gato(Felino):

    def get_sonido(self):
        return "Maullido"

    def get_alimentos(self):
        return "Ratones"

    def get_habitat(self):
        return "Doméstico"

    def get_nombre_cientifico(self):
        return "Felis silvestris catus"


if __name__ == "__main__":
    animales = [Gato(), Perro(), Lobo(), Leon()]

    for animal in animales:
        print(animal.get_nombre_cientifico())
        print(f"Sonido: {animal.get_sonido()}")
        print(f"Alimentos: {animal.get_alimentos()}")
        print(f"Hábitat: {animal.get_habitat()}")
        print()
