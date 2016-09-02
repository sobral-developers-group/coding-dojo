#!/vagrant/codingdojo/bin/python

import unittest
from romanos import converte_Romanos

class TestRomanos(unittest.TestCase):
    
    def test_receber_1_retorna_I(self):
        self.assertEqual(converte_Romanos(1), "I")

    def test_receber_5_retorna_V(self):
        self.assertEqual(converte_Romanos(5), "V")

    def test_receber_10_retorna_X(self):
        self.assertEqual(converte_Romanos(10), "X")

    def test_receber_50_retorna_L(self):
        self.assertEqual(converte_Romanos(50), "L")

    def test_receber_100_retorna_C(self):
        self.assertEqual(converte_Romanos(100), "C")

    def test_receber_500_retorna_D(self):
        self.assertEqual(converte_Romanos(500), "D")

    def test_receber_1000_retorna_M(self):
        self.assertEqual(converte_Romanos(1000), "M")

    def test_receber_2_retorna_II(self):
        self.assertEqual(converte_Romanos(2), "II")

    def test_receber_3_retorna_III(self):
        self.assertEqual(converte_Romanos(3), "III")

    def test_receber_30_retorna_XXX(self):
        self.assertEqual(converte_Romanos(30), "XXX")

    def test_receber_300_retorna_CCC(self):
        self.assertEqual(converte_Romanos(300), "CCC")

    def test_receber_3000_retorna_MMM(self):
        self.assertEqual(converte_Romanos(3000), "MMM")

    def test_receber_6_retorna_VI(self):
        self.assertEqual(converte_Romanos(6), "VI")

    def test_receber_7_retorna_VII(self):
        self.assertEqual(converte_Romanos(7), "VII")

    def test_receber_61_retorna_LXI(self):
        self.assertEqual(converte_Romanos(61), "LXI")

    def test_receber_156_retorna_CLVI(self):
        self.assertEqual(converte_Romanos(156), "CLVI")

    def test_receber_1120_retorna_MCXX(self):
        self.assertEqual(converte_Romanos(1120), "MCXX")

    def test_receber_555_retorna_DLV(self):
        self.assertEqual(converte_Romanos(555), "DLV")

if __name__ == '__main__':
    unittest.main()
