class Automobilis:
    metai = 0
    modelis = ""
    kuro_tipas = ""
    
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(f"Automobilio metai: {self.metai}, automobilio modelis : {self.modelis}, automobilio kuro tipas: {kuro_tipas}")
    
    def vaziuoti(self):
        print(f"{self.modelis} Vaziuoja")
    
    def stoveti(self):
        print(f"{self.modelis} Automobilis priparkuotas")
    
    def pildyti_degalu(self):
        print(f"{self.modelis} Degalai ipilti")
        

class Elektromobilis(Automobilis):
    
    def pildyti_degalu(self):  # pakeitem klases Automobilis metoda
        print(f"{self.modelis} Baterija ikrauta")
    
    def vaziuoti_autonomiskai(self):
        print(f"{self.modelis} Vaziuoja autonomiskai")
        
        
print("-"*80)
bmw = Automobilis(2016,"BMW 750li Xdrive","Bendzinas")
elektromobilis_1 = Elektromobilis(2022,"VW","Elektromobilis" )
print("-"*80)
bmw.vaziuoti()
bmw.stoveti()
bmw.pildyti_degalu()
print("-"*80)
elektromobilis_1.vaziuoti()
elektromobilis_1.stoveti()
elektromobilis_1.pildyti_degalu()
print("-"*80)