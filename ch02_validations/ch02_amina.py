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

#age=int(input("What is your age "))
#
#age=input("What is your age? ")
#age_int=int(age)

# -------------------- Task 3 --------------------------- #

#option=input("Please input yes or no ").lower() 

# -------------------- Task 4 --------------------------- #

 #---- Task 4 (Validating String Length)----# 
      
while True:
    age=input("What is your age? ") 
    if len(age) >= 3:
        print("Please enter a correct age! ")
    else:

        break

# ---------- Using an if/else statement ----------- #  

choice = input("Make a password?: ").lower()
UserInput = choice 

if len(UserInput) == 5 :
    print('You need more charcaters')
elif len(UserInput) == 7: 
    print('You still don\'t have enough characters')
else:
    print('Thank you for making your new password!')



# ------ Task 5 - Using while true inifinite loop ----- #

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
#  while choice < 2 or choice > 6:
#      choice = int(input('What is your choice '))
    
while True:
    try:
        while choice < 2 or choice > 6:
           choice = int(input('What is your choice '))
        break
    except ValueError:
        print('please type a number!')
        
# ---------- Task 6 - Indefinite While True Loop ------- #     

#Indefinite loop:
#def checking_input_two():
#   print("***choice***")
#   print('***choice***')    
#print('2. Display my name')
#print('4. Display my age')
#print('6. Display my city')
#
#while True:
#       choice=0
#       try:
#          while choice<2 or choice >6:
#               choice=int(input("what's your choice? "))
#               if choice == 2:
#                        print('Amina')
#               elif choice == 4:
#                        print('20 years old')
#               elif choice == 6:
#                        print('London')
#               else:
#                        print('Please try again')
##                 pass
#               break
#       except ValueError:
#           print("please type a number! ")
#           
#       else:
#           if choice<1 or choice >3:
#               print("Please put a correct choice.")
#
#checking_input_two() 
             
# ---------- Task 7 - validation using User input ------- #

#class Spam(object):
#    def __init__(self, description, value):
#        if not description or value <=0:
#            raise ValueError
#        self.description = description
#        self.value = value  
      
#s= Spam('s',5)
#print(s.value)
#print(s.description)
#----------------------------------------------------
#What is printed:
    #5
    #s
#----------------------------------------------------

#If you give the wrong input, it will raise a ValueError message:

#s=Spam('',-1)
#print(s.value)
    
#You can also rite the code with assert statements:
    
#class Spam(object):
#    def __init__(self, description, value):
#        assert description != ""
#        assert value > 0
#        self.description = description
#        self.value = value    
#        
#        
#s=Spam('',-1)
    
#print(s.value)
