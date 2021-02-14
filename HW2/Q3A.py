def compute_histogram(image):
    '''
    Computes histogram of the input image.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The numpy array of numbers in histogram.   
    '''
    
    histogram = np.zeros((256), np.int)
    
    ####### your code ########
    n,m=image.shape
    for i in range(0,n):
        for j in range(0,m):
            histogram[image[i,j]]+=1

                    
    ##########################
    
    return histogram


