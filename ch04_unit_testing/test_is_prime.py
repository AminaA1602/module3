# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:51:22 2019

@author: Skitt
"""
import unittest
from is_prime import is_prime



class prime_test(unittest.TestCase): # --> A class is being created to test all the possibilities/scenarios of the function created. It will run sequentially once it's finished. 
    """Tests for 'is_prime.py'"""
    def _test_is_five_prime(self):
        """ Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__== '__main__':
    unittest.main()























        