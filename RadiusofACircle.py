# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 19:06:43 2018

@author: KingDash
"""

# Input area and the calculate the radius of a circle
import math
Error="N"
PI=3.14
try:
    A=int(input('Enter the area of a circle in integer:'))
except ValueError:
    print('invalid entry')
    Error="Y"
except NameError:
    print('undefined entry')
    Error="Y"
    
if Error=="N":
    # calculate the radius
    r=math.sqrt(A/PI)
    
    print('The radius of the circle is ' + ' ' , r )