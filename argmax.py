# argmax from scratch

def argmax(vector):
    index, value = 0, vector[0]
    for i,v in enumerate(vector):
        if v > value:
            index, value = i,v
            return index
        
# Define vector
vector = [0.4, 0.5, 0.1]
# Get argmax
result = argmax(vector)
print('arg max of %s: %d' % (vector,result))

# argmax using numpy

from numpy import argmax
vector = [0.4, 0.5, 0.1]
result = argmax(vector)
print('arg max of %s: %d' % (vector, result))

# matrix of four rows

from numpy import argmax
from numpy import asarray
# define vector
probs = asarray([[0.4, 0.5, 0.1], [0.0, 0.0, 1.0], [0.9, 0.0, 0.1], [0.3, 0.3, 0.4]])
print(probs.shape)
# get argmax
result = argmax(probs, axis=1)
print(result)