import numpy as np

#Creates a random array but should not be used and the results are inconsistent.
a = np.random.randn(5)

#Create a random array
a = np.random.randn(5,1)
print (a)

#Prints the shape of the vector
print (a.shape)

#Print transpose of array a
print (a.T)

#Errors checking the type of the array
assert(a.shape == (5,1))

#Product of A and A traspose
print (np.dot(a,a.T))

