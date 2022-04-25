import datetime

class Darbuotojas():
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo


    def _kiek_dirba_valandu(self):
        nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y-%m-%d")
        dabar = datetime.datetime.today()
        skirtumas = dabar - nuo_kada_dirba
        return skirtumas.days * 8

    def paskaiciuoti_atlyginima(self):
        atlyginimas = self.valandos_ikainis * self._kiek_dirba_valandu()
        print(self.vardas + " uždirbo " + str(atlyginimas) + " Aaaauru")

class Normalus_darbuotojas(Darbuotojas):
    def _kiek_dirba_valandu(self):
        nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y-%m-%d")
        dabar = datetime.datetime.today()
        skirtumas = dabar - nuo_kada_dirba
        return (skirtumas.days * 8) / 7 * 5


kasparas = Darbuotojas("Kasparas", 40, "2019-10-3")
kasparas_normalus = Normalus_darbuotojas("Kasparas", 40, "1996-10-3")
kasparas.paskaiciuoti_atlyginima()
kasparas_normalus.paskaiciuoti_atlyginima()

