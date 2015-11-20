#!/vagrant/codingdojo/bin/python

import unittest
from jokenpo import Jokenpo

class Test_Jokenpo(unittest.TestCase):
        def test_Empate(self):
            self.assertEqual(Jokenpo('Pedra', 'Pedra'), 'Empate')
            self.assertEqual(Jokenpo('Tesoura', 'Tesoura'), 'Empate')
            self.assertEqual(Jokenpo('Papel','Papel'),'Empate')

        def test_tesoura_pedra(self):
            self.assertEqual(Jokenpo('Tesoura','Pedra'),'Pedra')
        def test_papel_pedra(self):
            self.assertEqual(Jokenpo('Papel', 'Pedra'), 'Papel')
        def test_tesoura_papel(self):
            self.assertEqual(Jokenpo('Tesoura','Papel'),'Tesoura')

        def test_papel_tesoura(self):
            self.assertEqual(Jokenpo('Papel','Tesoura'),'Tesoura')

        def test_pedra_papel(self):
            self.assertEqual(Jokenpo('Pedra', 'Papel'), 'Papel')
        def test_pedra_tesoura(self):
            self.assertEqual(Jokenpo('Pedra','Tesoura'),'Pedra')





if __name__ == '__main__':
    unittest.main()
