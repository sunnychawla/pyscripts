import math as m

def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    s = 1/(1+m.exp(-x))
    ### END CODE HERE ###
    
    return s

print (basic_sigmoid(3))
