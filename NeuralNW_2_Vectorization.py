import numpy as np

# Define an 4,3 array
A = np.array ([[56.0, 0.0, 4.4, 68.0],
               [1.2, 104.0, 52.0, 8.0],
               [1.8, 135.0, 99.0, 0.9]])
print(A)

#Sum each row in the array
cal = A.sum(axis=0)
print (cal)

#Calculate the percentage by dividing the 3,1 array A by 1,1 array cal and reshape the result 
percentage = 100*A/cal.reshape(1,4)
print (percentage)
