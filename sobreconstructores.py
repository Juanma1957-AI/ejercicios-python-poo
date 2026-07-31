class ArticuloCientifico:
    def __init__(
        self,
        titulo,
        autor,
        palabras_clave=None,
        publicacion=None,
        anio=None,
        resumen=None,
    ):
        self.titulo = titulo
        self.autor = autor
        self.palabras_clave = palabras_clave if palabras_clave is not None else []
        self.publicacion = publicacion
        self.anio = anio
        self.resumen = resumen

    def imprimir(self):
        print("Título del artículo =", self.titulo)
        print("Autor del artículo =", self.autor)
        print("Palabras clave =")
        for i in range(len(self.palabras_clave)):
            print(self.palabras_clave[i])
        print("Publicación =", self.publicacion)
        print("Año =", self.anio)
        print("Resumen =", self.resumen)


if __name__ == "__main__":
    palabras = ["Astrofísica", "Gravedad", "Cosmología"]

    articulo = ArticuloCientifico(
        "Sobre la electrodinámica de los cuerpos en movimiento",
        "Max Planck",
        palabras,
        "Revista de Física",
        1905,
        "Estudio sobre los principios del movimiento y campos electromagnéticos.",
    )

    articulo.imprimir()
