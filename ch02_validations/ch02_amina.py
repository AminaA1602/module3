# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:35:18 2019

@author: Skitt
"""
#print("What is your age?")
#age = int(input())
#type(age)
#
#option = input("Please choose yes or no: ").lower()

# ------- Task 1: Revise input function -------- #

print("What\'s your age? ")
Age = input()

# -------------------- Task 2 --------------------------- #


print("What is your age? ")
age = int(input())
type(age)

# --- > Other ways of casting this input: 

age=int(input("What is your age "))

age=input("What is your age? ")
age_int=int(age)

# -------------------- Task 3 --------------------------- #

option=input("Please input yes or no ").lower() 

# -------------------- Task 4 --------------------------- #

option=input("Please input yes or no ").ASBnda.lower() 

# ---------- Using an if/else statement ----------- #  

choice = input("Make a password?: ").lower()
UserInput = choice 

if len(UserInput) == 5 :
    print('You need more charcaters')
elif len(UserInput) == 7: 
    print('You still don\'t have enough characters')
else:
    print('Thank you for making your new password!')

    
####### Using while true inifinite loop ######## 

# -------------------- Task 5 --------------------------- #

print('***choice***')    
print('2. Display my name')
print('4. Display my age')
print('6. Display my city')

choice = int(input('What is your choice ')) 

if choice == 2:
    print('Amina')
elif choice == 4:
    print('20 years old')
elif choice == 6:
    print('London')
else:
    print('Please try again')


## ------ > To validate the user input: 
#    while choice < 2 or choice > 6:
#        choice = int(input('What is your choice '))
        

        
while True:
    try:
        while choice < 2 or choice > 6:
           choice = int(input('What is your choice '))
        break
    except ValueError:
        print('please type a number!')

# ---------- Class based user input validation ------- #

class Spam(object):
   def __init__(self,description,value):
        if not description or value <=0:
            raise ValueError
        self.description = description 
        self.value = value 
        print('Wrong input')

s = Spam('', -1)
v = Spam('hhhh', 5)

print(v.value)



