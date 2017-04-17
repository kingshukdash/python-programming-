# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:05:37 2017

@author: KingDash
"""
Error="N"
try:
    x=int(input('Enter an integer:'))
except ValueError:
    print('invalid entry')
    Error="Y"
except NameError:
    print('undefined entry')
    Error="Y"
    
if Error=="N":
    if x<0:
        y=x
        print(y, 'is a negetive number and converted to zero',x)
    elif x==0:
        print(x, 'is zero')
    elif x==1:
        print(x, 'is single')
    else:
        print(x, 'greater than zero and one')