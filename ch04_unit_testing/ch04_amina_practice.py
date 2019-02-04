# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 18:59:26 2019

@author: Skitt
"""

#Practice 1:
                           
# Unit testing involves testing small units of code in isolation to check for specfic responses/outputs 

import unittest

def checkPrime(number):
    '''This function checks if the number is a prime number'''
    if number == 2:
        return True
    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                return False
                break
            else:
                return True
                break
    else:
        return False

# ----- > Using classes to generate test cases
class CheckPrime(unittest.TestCase):

    def test_checkPrime(self):
        self.assertEqual(checkPrime(3), True)   
        #---- > Check if the function returns the value specified in the second argument

    def test_checkPrime2(self):
        self.assertTrue(checkPrime(5)) #---> Check if the function returns True
        self.assertFalse(checkPrime(4)) # --->  Check if the function returns False

# This tests checks that any string input produces an error
    def test_checkPrime3(self):
       
        with self.assertRaises(TypeError):
            checkPrime('1')

            
if __name__ == '__main__':
    unittest.main() # ----> This runs the Class tests in sequential order       
            
            
#Practice 2: Testing using a counter
    
#word_count = ("apple orange green red yello red yes no yes no happy yay")
def simple_statement(string):
    my_string = string.lower().split()
    my_dict = {}
    for item in my_string:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    print(my_dict)
    return my_dict
    