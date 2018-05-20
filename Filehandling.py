# -*- coding: utf-8 -*-
"""
Created on Sat May 19 17:25:21 2018

@author: KingDash
"""

#  to open a text file
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'Test.txt')
#testFile=open(filename)
#print(testFile.read())
file = open(filename,'r') 
print(file.read()) 
# create a text file

