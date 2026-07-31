class Pedido:
    def calcular_pedido(
        self,
        primer_plato,
        costo_primer_plato,
        bebida,
        costo_bebida,
        segundo_plato=None,
        costo_segundo_plato=0,
        postre=None,
        costo_postre=0,
    ):
        total = costo_primer_plato + costo_bebida + costo_segundo_plato + costo_postre

        platos = [primer_plato]
        if segundo_plato:
            platos.append(segundo_plato)
        platos.append(bebida)
        if postre:
            platos.append(postre)

        menu_ordenado = " + ".join(platos)
        print(f"El costo de {menu_ordenado} es = ${total:.1f}")


if __name__ == "__main__":
    orden1 = Pedido()
    orden1.calcular_pedido("Sopa de tomate", 8000, "Jugo de mango", 3500)

    orden2 = Pedido()
    orden2.calcular_pedido(
        "Ceviche",
        12000,
        "Lomo salteado",
        18000,
        "Limonada",
        4000,
    )

    orden3 = Pedido()
    orden3.calcular_pedido(
        "Ensalada César",
        9000,
        "Pasta Carbonara",
        15000,
        "Flan de leche",
        6000,
        "Cerveza artesanal",
        5000,
    )
