#!/vagrant/codingdojo/bin/python

import unittest
from cheque import cheque_extenso

class TestChequeExtenso(unittest.TestCase):
    # 1º dia
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

    # 2º dia
    def test_recebe_100_00_retorna_cem_reais(self):
        self.assertEqual(cheque_extenso(100.00), "cem reais")

    def test_recebe_200_00_retorna_duzentos_reais(self):
        self.assertEqual(cheque_extenso(200.00), "duzentos reais")

    def test_recebe_300_00_retorna_trezentos_reais(self):
        self.assertEqual(cheque_extenso(300.00), "trezentos reais")

    def test_recebe_500_00_retorna_quinhentos_reais(self):
        self.assertEqual(cheque_extenso(500.00), "quinhentos reais")

    def test_recebe_400_00_retorna_quatrocentos_reais(self):
        self.assertEqual(cheque_extenso(400.00),"quatrocentos reais")

    def test_recebe_600_00_retorna_seiscentos_reais(self):
        self.assertEqual(cheque_extenso(600.00),"seiscentos reais")

    def test_recebe_21_00_retorna_vinte_e_um_reais(self):
        self.assertEqual(cheque_extenso(21.00),"vinte e um reais")

    def test_recebe_33_00_retorna_trinta_e_tres_reais(self):
        self.assertEqual(cheque_extenso(33.00),"trinta e três reais")

    def test_recebe_201_00_retorna_duzentos_e_um_reais(self):
        self.assertEqual(cheque_extenso(201.00),"duzentos e um reais")

    def test_recebe_221_00_retorna_duzentos_e_vinte_e_um_reais(self):
        self.assertEqual(cheque_extenso(221.00),"duzentos e vinte e um reais")

    def test_recebe_101_00_retorna_cento_e_um_reais(self):
        self.assertEqual(cheque_extenso(101.00),"cento e um reais")

    def test_recebe_121_00_retorna_cento_e_vinte_e_um_reais(self):
        self.assertEqual(cheque_extenso(121.00),"cento e vinte e um reais")

    def test_recebe_999_00_retorna_novecentos_e_noventa_e_nove_reais(self):
        self.assertEqual(cheque_extenso(999.00),"novecentos e noventa e nove reais")







if __name__ == '__main__':
    unittest.main()
