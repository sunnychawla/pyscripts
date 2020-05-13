#import numpy as np

# example of np.exp
#x = np.array([1, 2, 3])
#print(np.exp(x)) # result is (exp(1), exp(2), exp(3))

# example of vector operation
#x = np.array([1, 2, 3])
#print (x + 3)


# GRADED FUNCTION: sigmoid

import numpy as np # this means you can access numpy functions by writing np.function() instead of numpy.function()

def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    s = 1/(1+np.exp(-x))
    ds = s*(1-s)

    ### END CODE HERE ###
    
    return ds

x = np.array([1, 2, 3])
print ("sigmoid_derivative(x) = " + str(sigmoid_derivative(x)))

