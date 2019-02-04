# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:26:19 2019

@author: Skitt
"""

import unittest
from ch04_amina import is_prime

#import sys

# ---------------------- Task 1 ------------------------------- # 
#class prime_test(unittest.TestCase):
#    def test_prime(self):
#        self.assertTrue(is_prime(5)) 
#        self.assertTrue(is_prime(sys.args[1]))
#        self.assertIsInstance(sys.argv[1], int)
#        
#    def sys_input(self):
#        self.assertIsInstance(sys.argv[1], int)

# ---------------------- Task 2 ------------------------------- # 
          
class Prime_Test(unittest.TestCase):
#    def test_prime(self):
#        self.assertTrue(is_prime(5)) 
#        self.assertTrue(is_prime(11)) 
#        self.assertTrue(is_prime(23))
#        self.assertTrue(is_prime(-5)) 
#        self.assertTrue(is_prime(293)) 
    #def test_prime_float(self):
        #self.assertTrue(is_prime(5.9)) 
#    def test_non_prime_numbers(self):
#        self.assertFalse(is_prime(4))
    def test_prime(self):
        self.assertFalse(is_prime(0)) 
    def test_negative_number(self):
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))

if __name__ == '__main__':
    unittest.main()