'''
2022 Тестируем на Python: unittest и pytest. Инструкция для начинающих
https://tproger.ru/articles/testiruem-na-python-unittest-i-pytest-instrukcija-dlja-nachinajushhih/

Только работа с Pytest
'''
# import pytest
from math import *

def square_eq_solver(a:float, b:float, c:float) -> list:
   '''
   Тестируемая функция
   '''
   print('\n a, b, c')
   print(' ',a, b, c)
   result = []
   discriminant = b * b - 4 * a * c

   if discriminant == 0:
       result.append(-b / (2 * a))
   elif discriminant > 0:  # <--- изменили условие, теперь
                           # при нулевом дискриминанте
                           # не будут вычисляться корни
       result.append((-b + sqrt(discriminant)) / (2 * a))
       result.append((-b - sqrt(discriminant)) / (2 * a))

   return result

def test_no_root():
   res = square_eq_solver(10, 0, 2)
   assert len(res) == 0

def test_single_root():
   res = square_eq_solver(10, 0, 0)
   assert len(res) == 1
   assert res == [0]

def test_multiple_root():
   res = square_eq_solver(2, 5, -3)
   assert len(res) == 2
   assert res == [0.5, -3]