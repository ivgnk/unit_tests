'''
Модуль unittest: тестируем свои программы
https://pythonworld.ru/moduli/modul-unittest.html
'''

import unittest
import sys
import numpy as np
import inspect

curr_test = 0

class TestStringMethods(unittest.TestCase):

      # def __init__(self, *args, **kwargs):
      #     super(TestStringMethods, self).__init__(*args, **kwargs)
      #     self.curr_test = 0

      def setUp(self):
          # print(inspect.currentframe().f_code.co_name)
          pass

      # def tearDown(self):
      #       print('curr_test = ', self.curr_test)
      #       self.curr_test +=1

      def test_upper(self):
          ''' test_upper '''
          print(inspect.currentframe().f_code.co_name)
          self.assertEqual('foo'.upper(), 'FOO')


      def test_isupper1(self):
          ''' test_isupper1 '''
          print(inspect.currentframe().f_code.co_name)
          self.assertTrue('FOO'.isupper())

      def test_isupper2(self):
          ''' test_isupper2 '''
          print(inspect.currentframe().f_code.co_name)
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


class MyTestCase(unittest.TestCase):
    def tearDown(self):
        global curr_test
        print('curr_test = ', curr_test)
        curr_test += 1

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    # @unittest.skipIf(np.__version__ < 1,
    #                  "not supported in this library version")
    # def test_format(self):
    #     # Tests that work for only a certain version of the library.
    #     pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass


if __name__ == '__main__':
    unittest.main()