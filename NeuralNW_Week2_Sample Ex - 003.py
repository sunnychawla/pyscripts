# GRADED FUNCTION: image2vector
import numpy as np
def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """
    print ("Shape of image", np.shape(image))
    print ("1st col of shape", np.shape(image)[0])
    print ("Ravel Function", np.ravel(image))
    ### START CODE HERE ### (≈ 1 line of code)
    v = np.reshape(image,(1,(np.shape(image)[0]*np.shape(image)[1]*np.shape(image)[2])))
    ### END CODE HERE ###
    
    return v

# This is a 3 by 3 by 2 array, typically images will be (num_px_x, num_px_y,3) where 3 represents the RGB values
image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])

print ("image2vector(image) = " + str(image2vector(image)))

print ("shape of image2vector(image) = " , np.shape((image2vector(image))))

newimage = np.array ([[ 0.67826139] [ 0.29380381] [ 0.90714982] [ 0.52835647] [ 0.4215251 ] [ 0.45017551] [ 0.92814219] [ 0.96677647] [ 0.85304703] [ 0.52351845] [ 0.19981397] [ 0.27417313] [ 0.60659855] [ 0.00533165] [ 0.10820313] [ 0.49978937] [ 0.34144279] [ 0.94630077]])

print (np.shape(newimage))

"""
image = np.array([[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]])

print (image)
print (np.shape(image))
print (np.ravel(image))
print (np.reshape(image,((np.shape(image)[1]),(np.shape(image)[0]))))
"""
