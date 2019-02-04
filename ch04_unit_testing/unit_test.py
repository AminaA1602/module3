# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:27:32 2019

@author: Skitt
"""
#import unittest


###Check if database is empty####
def checkIfTables():
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablesInDb =(c.fetchall())
print(len(tablesInDb))
print(tablesInDb)
if len(tablesInDb) > 0:
    print("Tables available.")
    return True
else:
    print("table unavailable")
    return False

####Check if tables in database are empty###
def checkIfTableEmpty():
    c.execute('SELECT * FROM business')
resultsRecords = c.fetchall()
if len(resultsRecords ) > 0:
    print("Table not empty")
    return True
else:
    print("Table is empty")
    return False
checkIfTableEmpty()


#c.close()
#conn.close()




##connect to the database##
#def getdb():
#    try:
#        conn = sqlite3.connect('phonebook.db')
#        c = conn.cursor()
#        return c
#    except:
#        return False