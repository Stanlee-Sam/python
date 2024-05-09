#add two list of number using pytho list and numpy array and compare them

import numpy as np
import time
import sys

size = 1000

#list
l1 = range(size)
l2 = range(size)

#array
a1 = np.arange(size)
a2 = np.arange(size)

#python list
startl = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
endl = time.time()
durationl = endl-startl
print("List took: ", durationl * 1000) #in millliseconds

#numpy array
starta = time.time()
result = a1 + a2
enda = time.time()
durationa = enda - starta
print("Numpy array took: ", durationa * 1000)

