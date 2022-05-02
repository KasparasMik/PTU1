import unittest

def skaiciu_suma(*args):
    return sum(args)

# skaiciu_suma(2, 6, 4, 78, 1, 454, 30, 68)

# print(skaiciu_suma(-1000, 1000))

def didziausias_skaicius(*args):
    return max(args)

# didziausias_skaicius(2, 5, 7, 9, 5, 12, 45, 900, 1000, 12)

def sakinys_atvirksciai(sakinys):
    sakinio_zodziai = sakinys.split()
    sarasas_atvirkciai = sakinio_zodziai[::-1]
    return " ".join(sarasas_atvirkciai)

# sakinys_atvirksciai("Jau pavasaris atėjo, kas čia plytų tiek pridėjo?")


def ar_yra(skaicius, sarasas):
    return (skaicius in sarasas)

# ar_yra(5, [5, 6, 7, 9, 10, 15, 45, 100])

def patikrinti_sakini(sakinys):
    zodziai = len(sakinys.split())
    skaiciai = sum(c.isdigit() for c in sakinys)
    didziosios = sum(c.isupper() for c in sakinys)
    mazosios = sum(c.islower() for c in sakinys)
    return (f"Žodžių kiekis: {zodziai}, Skaičių kiekis: {skaiciai}, Didžiųjų raidžių: {didziosios}, Mažųjų raidžių: {mazosios}")

# patikrinti_sakini("12: Jau pavasaris atėjo, kas čia plytų TIEK pridėjo?")


def lyginiai_skaiciai(nuo, iki):
    '''
    Atspausdina visus paduoto rėžio (nuo… iki) lyginius skaičius
    :param nuo: Mažiausias rėžio skaičius
    :param iki: Didžiausias rėžio skaičius
    :return: Lyginių skaičių sąrašas
    '''
    sarasas = []
    for skaicius in range(nuo, iki + 1):
        if skaicius % 2 == 0:
            sarasas.append(skaicius)
    return sarasas



print(lyginiai_skaiciai(0, 51))


##### UNIT TEST ####

class TestUzduotis1(unittest.TestCase):
    
    def test_skaiciu_suma(self):
        self.assertEqual(skaiciu_suma(2, 6, 4, 78, 1, 454, 30, 68), 643)
        self.assertEqual(skaiciu_suma(-2, 6, -4, -78, 1, 454, 0, 68), 445)
        self.assertEqual(skaiciu_suma(-1000, 1000), 0)


    def test_didziausias_skaicius(self):
        self.assertEqual(didziausias_skaicius(2, 5, 7, 9, 5, 12, 45, 900, 1000, 12), 1000)

    def test_sakinys_atvirksciai(self):
        self.assertEqual(sakinys_atvirksciai("Jau pavasaris atėjo, kas čia plytų tiek pridėjo?"), "pridėjo? tiek plytų čia kas atėjo, pavasaris Jau")

    def test_ar_yra(self):
        self.assertTrue(ar_yra(5, [5, 6, 7, 9, 10, 15, 45, 100]))

    def test_patikrinti_sakini(self):
        lukestis = "Žodžių kiekis: 9, Skaičių kiekis: 2, Didžiųjų raidžių: 5, Mažųjų raidžių: 34"
        self.assertEqual(patikrinti_sakini("12: Jau pavasaris atėjo, kas čia plytų TIEK pridėjo?"), lukestis)

    def test_lyginiai_skaiciai(self):
        self.assertEqual(lyginiai_skaiciai(0, 51), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

