# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:13:40 2019

@author: Skitt
"""
import pysqlite3

def getdb():
    conn = psyqlite3.connect('db/phonebook5)
    cursor = conn.cursor()
    return cursor 

def finBusiness(businessName, businessType,location):
    # returns all businessName, businessType location True 