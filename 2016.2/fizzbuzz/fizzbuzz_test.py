#!/usr/bin/python3.5

import unittest
from fizzbuzz import FizzBuzz
from fizzbuzz import FizzBuzzAll

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(FizzBuzz(1), 1)
        self.assertEqual(FizzBuzz(2), 2)
        self.assertEqual(FizzBuzz(5), 'Buzz')
        self.assertEqual(FizzBuzz(6), 'Fizz')
        self.assertEqual(FizzBuzz(9), 'Fizz')
        self.assertEqual(FizzBuzz(15), 'FizzBuzz')
        self.assertEqual(FizzBuzz(30), 'FizzBuzz')
        self.assertEqual(FizzBuzz(100), 'Buzz')

    def test_fizz_buzz_all(self):
       self.assertEqual(FizzBuzzAll(15), [1, 2, "Fizz", 4,
                                          "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
                                           11, "Fizz", 13, 14, "FizzBuzz"])





if __name__ == '__main__':
    unittest.main()
