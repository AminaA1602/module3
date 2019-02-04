# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 18:44:53 2019

@author: Skitt
"""


####################### Prime Numbers ##########################

# -------- Task 1 Return True if *number* is prime ---------- # 

 
#def is_prime(number):
#    for element in range(number):
#        if number % element ==0:
#            return False 
#    return True 


#-------------------------- Task 2  -------------------------#

def is_prime_2(number):
    """Return True if *number* is prime."""
    if number > 1: # ---> The test fails because the 0 is not included in the range therefore is incorrectly determined to be a prime number in the test.
        for element in range(2, number):
            if number % element == 0:
                return False
    return True


# ---- > The version below adds in a range meaning it will now take into account the value of 0 

    
def is_prime_3(number):
    """Return True if *number* is prime."""
    if number in (0, 1):
        return False
    else:
        for element in range(2, number):
            if number % element == 0:
                return False
    return True



def is_prime_4(number):
    """Return True if *number* is prime."""
    if number < 0: #---> This condition now accounts for all of the exceptions  raised, including negative numbers, 0 and 1.
        return False
    
    elif number in (0, 1):
        return False
    
    else:
        for element in range(2, number):
            if number % element == 0:
                return False
    return True
 

#----------------Task 3 (Prime Numbers)------------------#
 
# ---- > final version of the prime function:
          
def is_prime_final(number):
    if number <= 1:
        return False
    else:
        for element in range(2, number):
            if number % element == 0:
                return False
    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime_final(index):
            print(index)
         
          