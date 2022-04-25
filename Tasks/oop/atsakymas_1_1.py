# 1 Uzduotis  && 3 Uzduotis && 4 Uzduotis
class Sakinys:
    tekstas = ""
    
    def __str__(self):   # 4 uzduotis
        return str(self.tekstas)
    
    def __init__(self, tekstas=None):
        if tekstas == None: # 3 Uzduotis, jei nenurodom teksto sita pisa
            import this
            tekstas = "".join([this.d.get(c, c) for c in this.s]) # Zen of Python tekstas 
        self.tekstas = tekstas
        
    #1.1 Uzduotis
    def tekstas_atbulai(self):  # Self rodo i savo objekta
        return self.tekstas[::-1]
    # 1.2
    def tekstas_mazosiomis_raidemis(self):
        return self.tekstas.lower()
    #1.3
    def tekstas_didziosiomis_raidemis(self):
        return self.tekstas.upper()
    #1.4
    def zodis_pagal_eiles_numeri(self,numeris):
        zodziai = self.tekstas.split()
        return zodziai[numeris]
    #1.5
    def kiek_tekste_yra_zodziu(self):
        return str(len(self.tekstas.split())) + " Zodziai, ir " + str(len(self.tekstas)) + " Simboliai."
    #1.6
    def pakeicia_nurodyta_zodi(self,senas_zodis,naujas_zodis):
        return self.tekstas.replace(senas_zodis,naujas_zodis)
    #1.7
    def kiek_sakinyje_yra_zodziu_skaiciu_ir_etc(self):
        mazosios_raides = 0
        didziosios_raides = 0
        daugybos_simbolis = 0
        pliuso_simbolis = 0
        minuso_simbolis = 0
        kablelis = 0
        taskas = 0
        skaiciu_kiekis = 0
        for simbolis in self.tekstas:
            if simbolis.islower():
                mazosios_raides += 1
            elif simbolis.isupper():
                didziosios_raides += 1
            elif simbolis.isnumeric():
                skaiciu_kiekis += 1
            elif simbolis == "*" :
                daugybos_simbolis += 1
            elif simbolis == "+":
                pliuso_simbolis += 1
            elif simbolis == "-":
                minuso_simbolis += 1
            elif simbolis == ",":
                kablelis += 1
            elif simbolis == ".":
                taskas += 1
        return f"Tekste yra: {mazosios_raides} mazuju raidziu, {didziosios_raides} didziuju raidziu, {daugybos_simbolis} daugybos simboliu, {pliuso_simbolis} pliuso simboliu, {minuso_simbolis} minuso simboliu, {kablelis} kableliu ir {taskas} tasku bei {skaiciu_kiekis} skaiciu."
                
           
            


tekstas1 = Sakinys()
print(tekstas1) # grazina objekto ID
print("-"*80)
print(tekstas1.tekstas) # spausdina teksta, kuri nurodem tekstas 1 stringe
print("-"*80)
print(tekstas1.tekstas_atbulai())
print("-"*80)
print(tekstas1.tekstas_mazosiomis_raidemis())
print("-"*80)
print(tekstas1.tekstas_didziosiomis_raidemis())
print("-"*80)
print(tekstas1.zodis_pagal_eiles_numeri(0))
print(tekstas1.zodis_pagal_eiles_numeri(2))
print("-"*80)
print(tekstas1.kiek_tekste_yra_zodziu())
print("-"*80)
print(tekstas1.pakeicia_nurodyta_zodi("Pirmas","Antras")) # pakeitem zodi nurodyta
print("-"*80)
print(tekstas1.kiek_sakinyje_yra_zodziu_skaiciu_ir_etc())

