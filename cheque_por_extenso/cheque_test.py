#!/vagrant/codingdojo/bin/python

import unittest
from cheque import cheque_extenso

class TestChequeExtenso(unittest.TestCase):

    def test_recebe_1_00_retorna_um_real(self):
        self.assertEqual(cheque_extenso(1.00), "um real")

    def test_recebe_2_00_retorna_dois_reais(self):
        self.assertEqual(cheque_extenso(2.00), "dois reais")

    def test_recebe_11_00_retorna_onze_reais(self):
        self.assertEqual(cheque_extenso(11.00), "onze reais")

    def test_recebe_15_00_retorna_quinze_reais(self):
        self.assertEqual(cheque_extenso(15.00), "quinze reais")

    def test_recebe_10_00_retorna_dez_reais(self):
        self.assertEqual(cheque_extenso(10.00), "dez reais")

    def test_recebe_20_00_retorna_vinte_reais(self):
        self.assertEqual(cheque_extenso(20.00), "vinte reais")

    def test_recebe_30_00_retorna_trinta_reais(self):
        self.assertEqual(cheque_extenso(30.00), "trinta reais")

    def test_recebe__18_retorna_dezoito_reais(self):
        self.assertEqual(cheque_extenso(18.00), "dezoito reais")










if __name__ == '__main__':
    unittest.main()
