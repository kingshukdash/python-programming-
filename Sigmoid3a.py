# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 00:44:18 2017

@author: KingDash
"""

import math
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10., 10., 0.2) 
def sigmoid(x):
    a = []
    for i in x:
        a.append(1/(1+math.exp(-i)))
    return a

def hyperbolicTangent(x):
    a = []
    for i in x:
        a.append(math.tanh(i))
    return a


sig = sigmoid(x)
hypTan = hyperbolicTangent(x)

plt.subplot(221)
plt.plot(x,sig)
#plt.yscale('Sigmoid')
plt.title('Sigmoid')
plt.grid(True)

plt.subplot(222)
plt.plot(x,hypTan)
#plt.yscale('hyperbolicTangent')
plt.title('hyperbolicTangent')
plt.grid(True)

plt.show()