def gaussian_filter(size, std):
    '''
    Creates the Guassian kernel with given size and std.
    
    Parameters:
        size (int): The size of the kernel. It must be odd.
        std (float): The standard deviation of the kernel.
    
    Returns:
        numpy.ndarray: The Guassina kernel.
    '''
    
    kernel = np.zeros((size,size), np.float)
    
    ####### your code ########
    coe=1/(2*((np.pi)*(std**2)))
    co2_std=2*(std**2)
    for i in range(size):
        for j in range(size):
            kernel[i,j]+=(coe*np.exp((-(i**2+j**2)/co2_std)))
    
    ##########################
    
    return kernel

def opencv_filter(img):
    '''
    Applys the OpenCV's guassian blur function on input image.
    
    Parameters:
        img (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The result image.
    '''
    
    out = None
    ####### your code ########
    
    out = cv2.GaussianBlur(img,(3,3),0)
    
    ##########################
    
    return out

