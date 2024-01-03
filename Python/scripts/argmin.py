# Argmin from scratch
def argmin(vector):
    index, value = 0, vector[0]
    for i,v in enumerate(vector):
        if v < value:
            index, value = i,v
            return index
        
vector = [0.3, 0.5, 0.3]
result = argmin(vector)
print('argmin of %s: %d' % (vector, result))

# Using numpy
from numpy import argmin
vector = [0.4, 0.5, 0.1]
result = argmin(vector)
print('arg min of %s: %d' % (vector, result))
