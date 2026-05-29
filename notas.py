import math
import tkinter as tk
from tkinter import messagebox


class Notas:
    def __init__(self):
        
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
       
        promedio = self.calcular_promedio()
        suma = sum(pow(nota - promedio, 2) for nota in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_mayor(self):
        
        return max(self.lista_notas)

    def calcular_menor(self):
        
        return min(self.lista_notas)


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.notas_obj = Notas()
        
        
        self.campos = []
        for i in range(5):
            tk.Label(self, text=f"Nota {i+1}:").place(x=20, y=20 + (i * 30))
            ent = tk.Entry(self)
            ent.place(x=105, y=20 + (i * 30), width=135)
            self.campos.append(ent)
            
        # botone calucar y limpiar[6, 8]
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=20, y=180, width=100)
        
        self.btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.place(x=140, y=180, width=100)
        
        # etiq resultados [6, 8]
        self.lbl_promedio = tk.Label(self, text="Promedio = ", justify="left")
        self.lbl_promedio.place(x=20, y=220)
        
        self.lbl_desviacion = tk.Label(self, text="Desviación estándar = ", justify="left")
        self.lbl_desviacion.place(x=20, y=250)
        
        self.lbl_mayor = tk.Label(self, text="Nota mayor = ", justify="left")
        self.lbl_mayor.place(x=20, y=280)
        
        self.lbl_menor = tk.Label(self, text="Nota menor = ", justify="left")
        self.lbl_menor.place(x=20, y=310)

    def calcular(self):
        try:
            for i in range(5):
                self.notas_obj.lista_notas[i] = float(self.campos[i].get())
            
            # resultados formateados [5, 9]
            self.lbl_promedio.config(text=f"Promedio = {self.notas_obj.calcular_promedio():.2f}")
            self.lbl_desviacion.config(text=f"Desviación estándar = {self.notas_obj.calcular_desviacion():.2f}")
            self.lbl_mayor.config(text=f"Nota mayor = {self.notas_obj.calcular_mayor()}")
            self.lbl_menor.config(text=f"Nota menor = {self.notas_obj.calcular_menor()}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

    def limpiar(self):
       
        for campo in self.campos:
            campo.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación estándar = ")
        self.lbl_mayor.config(text="Nota mayor = ")
        self.lbl_menor.config(text="Nota menor = ")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop() 
