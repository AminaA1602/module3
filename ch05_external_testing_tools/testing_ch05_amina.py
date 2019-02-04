# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:37:38 2019

@author: Skitt
"""

 #---- Task (External Testing Tools)----#
 
import unittest
from ch05_amina import Calculator

class TddInPythonExample(unittest.TestCase):
    
    def test_calculator_add_method_returns_correct_result(self):
        self.calc = Calculator()
        result = self.calc.add(2,2)
        self.assertEqual(4, result)
#        result= self.calc.add(5,"three")
#        self.assertEqual(8, result)   #returns type error as expected.
    def test_calculator_subtract_method_returns_correct_result(self):
        self.calc = Calculator()
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(9, 0.2)
        self.assertEqual(8.8, result)
    def test_calculator_multiply_method_returns_correct_result(self):
        self.calc = Calculator()
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(9, 0.2)
        self.assertEqual(1.8, result)
    def test_calculator_divide_method_returns_correct_result(self):
        self.calc = Calculator()
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(9, 0.2)
        self.assertEqual(45, result)
        
        
   
        
if __name__ == '__main__':
    unittest.main()