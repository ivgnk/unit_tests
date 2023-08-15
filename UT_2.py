'''
Модуль unittest: тестируем свои программы
https://pythonworld.ru/moduli/modul-unittest.html
'''

import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      ''' test_upper '''
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper1(self):
      ''' test_isupper1 '''
      self.assertTrue('FOO'.isupper())

  def test_isupper2(self):
      ''' test_isupper2 '''
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      ''' test_split '''
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

  def test_split2(self):
      ''' test_split2 '''
      s = 'hello world'
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()