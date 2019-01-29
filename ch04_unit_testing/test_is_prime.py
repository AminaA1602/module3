# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:51:22 2019

@author: Skitt
"""
#import unittest
#import sys 
#from is_prime import is_prime
#
#class prime_test(unittest.TestCase): # --> A class is being created to test all the possibilities/scenarios of the function created. It will run sequentially once it's finished. 
#    def test_prime(self):
#        self.assertIsInstance(sys[1],int) # --- > This is testing whether the output will be an integer. 
#        self.assertTrue(is_prime(5))

import unittest
from is_prime import is_prime

class prime_test(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(5.3)) 

unittest.main()























        