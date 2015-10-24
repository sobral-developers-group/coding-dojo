#!/vagrant/codingdojo/bin/python

import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_FizzBuzz_recebe_numero_simples(self):
        self.assertEqual(FizzBuzz(1), 1)
        self.assertEqual(FizzBuzz(2), 2)
        self.assertEqual(FizzBuzz(4), 4)

    def teste_Multiplo_de_3(self):
        self.assertEqual(FizzBuzz(3), "fizz")


    def teste_FizzBuzz_de_5(self):
        self.assertEqual(FizzBuzz(5), "buzz")
        self.assertEqual(FizzBuzz(10),"buzz")


    def teste_FizzBuzz_de_3_e_5(self):
        self.assertEqual(FizzBuzz(30),"fizzbuzz" )


if __name__ == '__main__':
    unittest.main()
