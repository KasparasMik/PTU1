from datetime import datetime,timedelta   
# 2 Uzduototis && 3 uzduotis && 4 uzduotis
class Sukaktis:
    data = ""
    
    def __str__(self):   # 4 uzduotis
        return str(self.data)
    
    def __init__(self,data):
        self.data = data
    #2.1
    def skirtumas_nuo_dabar(self):   # Round suapvalina
        skirtumas = datetime.now() - self.data
        skirtumas_metais = round(skirtumas.days // 365)
        skirtumas_menesiais = round(skirtumas.days / 365 * 12)
        skitumas_savaitemis =  round(skirtumas.days // 7)
        skirtumas_dienomis = round(skirtumas.days)
        skirtumas_valandomis = round(skirtumas.total_seconds() / 3600)
        skirtumas_minutemis = round(skirtumas.total_seconds() / 60)
        skirtumas_sekundemis = round(skirtumas.total_seconds())
        return (skirtumas_metais,skirtumas_menesiais ,skitumas_savaitemis, skirtumas_dienomis,skirtumas_valandomis,skirtumas_minutemis,skirtumas_sekundemis)
    #2.2
    def ar_keliamieji_metai(self):
        if self.data.year % 400 == 0 or (self.data.year % 100 != 0 and self.data.year % 4 == 0):
            return True
        else:
            return False
    #2.3
    def atimtis_is_nurodytos_datos(self,kiek_dienu):
        return (self.data - timedelta(days = kiek_dienu)).date()   # timedelta tai funkcijam, kuri tipo irasai (5) ir prideda 5 dienas pvz, klasese galima ir valandas ir pan. Ciatiesiog funkcija kuri padaro datos formata
    def sudetis_is_nurodytos_datos(self,kiek_dienu):
        return (self.data + timedelta(days = kiek_dienu)).date()


sukaktis1 = Sukaktis(datetime(1996,10,3,22,55,55,55555))
print(sukaktis1.skirtumas_nuo_dabar())
print("-"*80)
print(sukaktis1.ar_keliamieji_metai()) # Metai keliamieji ! 
print("-"*80)
print(sukaktis1.atimtis_is_nurodytos_datos(5)) # grazina data po nurodytos atimties
print("-"*80)
print(sukaktis1.sudetis_is_nurodytos_datos(5)) # grazina data po nurodytos prideties
print("-"*80)
