class Personas :
    @staticmethod
    def edalber (edjuan):
        edalber = (2*edjuan)/3
        return edalber 
    @staticmethod
    def edana (edjuan):
        edana = (4*edjuan)/3
        return edana
    @staticmethod
    def edmama (edjuan, edalber , edana):
        edmama = edalber + edana + edjuan
        return edmama
edjuan = 9
edalber = Personas.edalber (edjuan)
edana = Personas.edana (edjuan)
edmama = Personas.edmama (edjuan, edalber , edana)
print (f" Las edades son : Alberto {edalber}, Juan {edjuan}, Ana {edana}, Mama {edmama}")