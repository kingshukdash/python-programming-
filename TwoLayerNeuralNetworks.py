# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 23:21:48 2018

@author: KingDash
"""

# Two layer Neural Network
import math
import matplotlib.pyplot as plt
import numpy as np

# sigmoid function

def sigmoid(x, deriv=False):
    if (deriv==True):
          return x*(1-x)
    return  1/(1+np.exp(-x))

#  Input dataset matrix where each row is a training example

X = np.array([  [0,0,1],
             [0,1,1],
             [1,0,1],
             [1,1,1] ])
    
# Output dataset matrix where each row is a training example          

y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation  deterministic 

np.random.seed(1)
# initialize weights randomly with mean 0
#synapse0= First layer of weights, Synapse 0, connecting l0= Input Layer to l1= Hidden layer.
synapse0= 2*np.random.random((3,1)) - 1

for iter in range(10000):
# forward propagation
# I0=First Layer of the Network, specified by the input data

   l0 = X
 #I1= Second Layer of the Network, otherwise known as the hidden layer
   l1 = sigmoid(np.dot(l0,syn0))
# how much did we miss?
   l1_error = y - l1
# multiply how much we missed by the  slope of the sigmoid at the values in l1
   l1_delta = l1_error * sigmoid(l1,True)
  

# update weights
   synapse0 += np.dot(l0.T,l1_delta)

print ("Output After Training:" , l1)
