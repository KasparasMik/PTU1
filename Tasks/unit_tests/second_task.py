import unittest


class StringTriukai():
    def __init__(self, sakinys):
        self.sakinys = sakinys

    def pirmas_zodis(self):
        zodziai = self.sakinys.split()
        return zodziai[0]

    def paskutinis_zodis(self):
        zodziai = self.sakinys.split()
        return zodziai[-1]

    def atbulai(self):
        return self.sakinys[::-1]

    def nuo_galo(self):
        zodziai = self.sakinys.split()
        atvirksciai = zodziai[::-1]
        return " ".join(atvirksciai)

    def didziosiomis(self):
        return self.sakinys.upper()

    def mazosiomis(self):
        return self.sakinys.lower()

    def info(self):
        zodziai = len(self.sakinys.split())
        skaiciai = sum(c.isdigit() for c in self.sakinys)
        didziosios = sum(c.isupper() for c in self.sakinys)
        mazosios = sum(c.islower() for c in self.sakinys)
        return (f"Žodžių kiekis: {zodziai}, Skaičių kiekis: {skaiciai}, Didžiųjų raidžių: {didziosios}, Mažųjų raidžių: {mazosios}")


sakinys = StringTriukai("Laba diena, Lietuva")

print(sakinys.pirmas_zodis())
print(sakinys.paskutinis_zodis())
print(sakinys.atbulai())
print(sakinys.nuo_galo())
print(sakinys.didziosiomis())
print(sakinys.mazosiomis())
print(sakinys.info())

### UNIT TEST ### 

class TestUzduotis14_2(unittest.TestCase):
    
    def setUp(self):
        self.objektas = StringTriukai("Laba diena, Lietuva")

    def test_pirmas_zodis(self):
        self.assertEqual(self.objektas.pirmas_zodis(), "Laba")

    def test_paskutinis_zodis(self):
        self.assertEqual(self.objektas.paskutinis_zodis(), "Lietuva")

    def test_atbulai(self):
        self.assertEqual(self.objektas.atbulai(), "avuteiL ,aneid abaL")

    def test_nuo_galo(self):
        self.assertEqual(self.objektas.nuo_galo(), "Lietuva diena, Laba")

    def test_didziosiomis(self):
        self.assertEqual(self.objektas.didziosiomis(), "LABA DIENA, LIETUVA")

    def test_mazosiomis(self):
        self.assertEqual(self.objektas.mazosiomis(), "laba diena, lietuva")

    def test_info(self):
        lukestis = "Žodžių kiekis: 3, Skaičių kiekis: 0, Didžiųjų raidžių: 2, Mažųjų raidžių: 14"
        self.assertEqual(self.objektas.info(), lukestis)