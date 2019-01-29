# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:58:09 2019

@author: Skitt
"""

# -------------- Task 1  -------------  # 

try: 
    f = open('estfile')
except Exception:
    print('Sorry this file does not exist, or the file name is wrong. Please double check.')
    
 --- > corrected code:
 
try:
    f=open('testfile.txt')
except Exception:
    print('Error!')

# ------------ Dealing with multiple errors  -----------  #

try: 
    f = open('testfile.txt')
    s1 = not_exists
except Exception as e: 
    print('Sorry this file does not exist, or the file name is wrong. Please double check') # ---> The same error is printed out even though the file function has been corrected. There is now an error below this. 

try: 
    f=open('testfile.txt')
    s1= not_exist
except FileNotFoundError: # --> Using specific exceptions to filter out the error reporting process. 
    print('Sorry this file does not exists, or the file name is wrong. Plese double check.' )

# -------------- Task 2: Multiple exceptions  -------------  # 

try: 
    f=open('testfile.txt')
    s1=not_exist
except FilNotFoundError:
   print('Sorry this file does not exists, or the file name is wrong. Plese double check.' )
except Exception: 
    print('Sorry. Something is wrong after opening function.')


# -------------- Task 3  -------------  # 

try: 
    f = open('testfile.txt')
    s1= not_exist
except Exception as e: 
    print(e)

# -------------- Task 4: Else block  -------------  # 

try: 
    f = open('testfile.txt')
    s1= not_exist
except Exception as e: 
    print(e)
else:
    print(f.read())
    f.close() 

# -------------- Task 5: Finally block  -------------  # 

try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally...')
    
try: 
    f= open('testfile.txt')
except Exception as e: # -- > this is now acting as a debigging tool 
    print(e)
else:
    print(f.read()) 
    f.close()
finally: 
    print('Executing finally...')


# -- Task 6 : Further testing/manually raise a exception -- # 

try: 
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
         raise Exception
except Exception as e: 
    print('File name are the same')



    