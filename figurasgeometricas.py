import math
import tkinter as tk
from tkinter import messagebox
## Figura Geometrica
class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0
        self.superficie = 0

    def set_volumen(self, volumen):
        self.volumen = volumen

    def set_superficie(self, superficie):
        self.superficie = superficie

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie

## Cilindro

class Cilindro(FiguraGeometrica):

    def __init__(self, radio, altura):
        super().__init__()

        self.radio = radio
        self.altura = altura

        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.altura * (self.radio ** 2)

    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_bases = 2 * math.pi * (self.radio ** 2)

        return area_lateral + area_bases

# Esfera
class Esfera(FiguraGeometrica):

    def __init__(self, radio):
        super().__init__()

        self.radio = radio

        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        return 4 * math.pi * (self.radio ** 2)

# Piramide

class Piramide(FiguraGeometrica):

    def __init__(self, base, altura, apotema):
        super().__init__()

        self.base = base
        self.altura = altura
        self.apotema = apotema

        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lateral = 2 * self.base * self.apotema

        return area_base + area_lateral

## Cilindro
class VentanaCilindro(tk.Toplevel):

    def __init__(self):
        super().__init__()

        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)

        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=120, y=20)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=50)

        self.btn_calcular = tk.Button(
            self,
            text="Calcular",
            command=self.calcular
        )
        self.btn_calcular.place(x=120, y=80)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):")
        self.lbl_volumen.place(x=20, y=120)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):")
        self.lbl_superficie.place(x=20, y=150)

    def calcular(self):

        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())

            cilindro = Cilindro(radio, altura)

            self.lbl_volumen.config(
                text=f"Volumen (cm3): {cilindro.calcular_volumen():.2f}"
            )

            self.lbl_superficie.config(
                text=f"Superficie (cm2): {cilindro.calcular_superficie():.2f}"
            )

        except:
            messagebox.showerror(
                "Error",
                "Campo nulo o error en formato de número"
            )
## Ventana esfera
class VentanaEsfera(tk.Toplevel):

    def __init__(self):
        super().__init__()

        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)

        tk.Label(self, text="Radio (cms):").place(x=20, y=20)

        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=120, y=20)

        self.btn_calcular = tk.Button(
            self,
            text="Calcular",
            command=self.calcular
        )
        self.btn_calcular.place(x=120, y=60)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):")
        self.lbl_volumen.place(x=20, y=100)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):")
        self.lbl_superficie.place(x=20, y=130)

    def calcular(self):

        try:
            radio = float(self.campo_radio.get())

            esfera = Esfera(radio)

            self.lbl_volumen.config(
                text=f"Volumen (cm3): {esfera.calcular_volumen():.2f}"
            )

            self.lbl_superficie.config(
                text=f"Superficie (cm2): {esfera.calcular_superficie():.2f}"
            )

        except:
            messagebox.showerror(
                "Error",
                "Campo nulo o error en formato de número"
            )
# V Piramide
class VentanaPiramide(tk.Toplevel):

    def __init__(self):
        super().__init__()

        self.title("Pirámide")
        self.geometry("300x250")
        self.resizable(False, False)

        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=20)

        tk.Label(self, text="Altura (cms):").place(x=20, y=60)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=60)

        tk.Label(self, text="Apotema (cms):").place(x=20, y=100)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=120, y=100)

        self.btn_calcular = tk.Button(
            self,
            text="Calcular",
            command=self.calcular
        )
        self.btn_calcular.place(x=120, y=140)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):")
        self.lbl_volumen.place(x=20, y=180)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):")
        self.lbl_superficie.place(x=20, y=210)

    def calcular(self):

        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())

            piramide = Piramide(base, altura, apotema)

            self.lbl_volumen.config(
                text=f"Volumen (cm3): {piramide.calcular_volumen():.2f}"
            )

            self.lbl_superficie.config(
                text=f"Superficie (cm2): {piramide.calcular_superficie():.2f}"
            )

        except:
            messagebox.showerror(
                "Error",
                "Campo nulo o error en formato de número"
            )

## V Principal
class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Figuras Geométricas")
        self.geometry("350x160")
        self.resizable(False, False)

        self.btn_cilindro = tk.Button(
            self,
            text="Cilindro",
            command=self.abrir_cilindro
        )

        self.btn_cilindro.place(x=20, y=50, width=80)

        self.btn_esfera = tk.Button(
            self,
            text="Esfera",
            command=self.abrir_esfera
        )

        self.btn_esfera.place(x=125, y=50, width=80)

        self.btn_piramide = tk.Button(
            self,
            text="Pirámide",
            command=self.abrir_piramide
        )

        self.btn_piramide.place(x=225, y=50, width=100)

    def abrir_cilindro(self):
        VentanaCilindro()

    def abrir_esfera(self):
        VentanaEsfera()

    def abrir_piramide(self):
        VentanaPiramide()

if __name__ == "__main__":

    app = VentanaPrincipal()
    app.mainloop()

