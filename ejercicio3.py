class Calcular :
    @staticmethod
    def salario_bruto(htrabajo, phora):
        return (htrabajo * phora )
    @staticmethod
    def vretefuente(porcentaje_retefuente, salario_bruto):
        return (porcentaje_retefuente * salario_bruto)
    @staticmethod
    def salario_neto(salario_bruto, vretefuente):
        return (salario_bruto - vretefuente)


htrabajo = 48
phora = 5000
retefuente = 12.5
porcentaje_retefuente = 12.5/100

salario_bruto =Calcular.salario_bruto(htrabajo, phora)
vretefuente = Calcular.vretefuente(porcentaje_retefuente, salario_bruto)
salario_neto =Calcular.salario_neto(salario_bruto, vretefuente)
print(f"Salario bruto: {salario_bruto:,.0f}")
print(f"Retención en la fuente: {vretefuente:,.0f}")
print(f"Salario neto: {salario_neto:,.0f}")
