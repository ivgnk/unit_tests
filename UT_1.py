'''
2009 Тестирование в Python – объектно-ориентированный и процедурный подход
https://www.rsdn.org/article/python/PythonTesting.xml
'''

import unittest
from unittest import TestCase, main

import my_math
from my_math import factorial

class FactorialTestCase(TestCase):
    def test_fact_0(self):
        """test factorial(0)"""
        self.assertEqual(1, factorial(0))
    def test_fact_1(self):
        """test factorial(1)"""
        self.assertEqual(1, factorial(1))
    def test_fact_2(self):
        """test factorial(2)"""
        self.assertEqual(2, factorial(2))
    def test_fact_3(self):
        """test factorial(3)"""
        self.assertEqual(6, factorial(3))

if __name__ == '__main__':
    main()