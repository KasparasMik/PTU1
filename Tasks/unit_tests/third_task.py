import unittest


def kmi(svoris, ugis):
    if svoris < 30:
        raise ValueError("Svoris per mažas")
    if svoris > 200:
        raise ValueError("Svoris per didelis")
    if ugis < 1.0:
        raise ValueError("Ūgis per mažas")
    if ugis > 3.0:
        raise ValueError("Ūgis per didelis")
    return svoris / (ugis**2)


### UNIT TEST ### 

class TestSkaiciavimas(unittest.TestCase):
    def test_kmi(self):
        self.assertEqual(kmi(78, 1.82), 23.54788069073783)
        self.assertEqual(kmi(50, 1.56), 20.5456936226167)
        self.assertEqual(kmi(100, 1.90), 27.70083102493075)
        with self.assertRaises(ValueError):
            kmi(20, 1.40)
        with self.assertRaises(ValueError):
            kmi(240, 1.40)
        with self.assertRaises(ValueError):
            kmi(80, 0.40)
        with self.assertRaises(ValueError):
            kmi(80, 3.40)