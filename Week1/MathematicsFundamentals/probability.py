# learning implementations of probability concepts using numpy library
import numpy as np

# creating an array of random numbers 
array = np.random.rand(3,4)
print("An array of 3x4 with random values from [0-1)")
print(array)
array1 = np.random.randint(2, 50, size = (3,3))
print("A sqaure array of size 3x3 with values in range [2-50)")
print(array1)
eye = np.eye(5)
print("An Zero matrix of arbitratry size 2,5")
zeroes = np.zeros((2,5))
print(zeroes)
print("An Identity matrix of size 5x5")
print(eye)




