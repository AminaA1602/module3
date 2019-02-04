# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:57:12 2019

@author: Skitt
"""

#-------------- Unit testing with OOP (classes) -------------- #
          
class Calculator():
    def add(self, x,y): 
        return x+y
    
    def subtract(self,x,y): 
        return x - y 
    def multiply(self,x,y): 
        return x * y 
    def divide(self,x,y): 
        if y==0: 
            return "You can't divide by zero!" 
        else: 
            return x/y 
    