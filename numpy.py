import numpy
import sys
import time

#create list with 1000 elements
l = list(range(1000))
#print size of list
print(sys.getsizeof(l)*len(l))

#create array
array = numpy.arange(1000)
print(array.size * array.itemsize)
