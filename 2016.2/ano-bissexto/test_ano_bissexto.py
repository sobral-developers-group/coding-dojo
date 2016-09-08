#!/usr/bin/python3.5

import unittest

from is_bissexto import is_bissexto

class TestAnoBissexto(unittest.TestCase):
    def test_ano_bissexto(self):
        self.assertEqual(is_bissexto(4),   True)
        self.assertEqual(is_bissexto(8),   True)
        self.assertEqual(is_bissexto(1732),True)
        self.assertEqual(is_bissexto(400), True)
        self.assertEqual(is_bissexto(1200),True)
        self.assertEqual(is_bissexto(1944),True)
        self.assertEqual(is_bissexto(2008),True)
        self.assertEqual(is_bissexto(1888),True)
        self.assertEqual(is_bissexto(1600),True)

    def test_ano_nao_bissexto(self): 
        self.assertEqual(is_bissexto(1),   False)
        self.assertEqual(is_bissexto(5),   False)
        self.assertEqual(is_bissexto(100), False)
        self.assertEqual(is_bissexto(1000),False)
        self.assertEqual(is_bissexto(1889),False)    


if __name__ == '__main__':
    unittest.main()