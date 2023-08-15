'''
2009 Тестирование в Python – объектно-ориентированный и процедурный подход
https://www.rsdn.org/article/python/PythonTesting.xml

https://docs.python.org/3/library/unittest.html
https://docs.python.org/3.11/library/unittest.html#unittest.TestCase.assertEqual
'''

import unittest
import os
from unittest import TestCase, main

import my_math
from my_math import factorial
import inspect

class FactorialTestCase(TestCase):
    '''
    импортируем из модуля unittest класс TestCase,
    создаем производный от него класс FactorialTestCase,
    определяем в классе FactorialTestCase несколько тестов
    '''
    def test_fact_0(self):
        """test factorial(0)"""
        self.assertEqual(1, factorial(0))
    def test_fact_1(self):
        """test factorial(1)"""
        self.assertEqual(1, factorial(1))

class FactorialTestCase2(TestCase):
    def test_fact_2(self):
        """test factorial(2)"""
        self.assertEqual(2, factorial(2))
    def test_fact_3(self):
        """test factorial(3)"""
        self.assertEqual(6, factorial(3))


if __name__ == '__main__':
    # вызываем определенную в модуле unittest функцию main,
    # которая находит созданный нами класс, в нем находит
    # все тесты (т.е. все методы, имена которых начинаются с приставки «test»)

    main()