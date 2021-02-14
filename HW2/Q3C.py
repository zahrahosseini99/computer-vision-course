def histogram_stretching(image):
    '''
    Streches the histogram of the input image.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The result image that it's histogram be streched.   
    '''
    
    h = compute_histogram(image)
    out_image = image.copy()

    ####### your code ########
    max_color=image.max()
    min_color=image.min()
    m,n=image.shape
    for i in range(m):
            for j in range(n):
              out_image[i,j]=((image[i,j]-min_color)/(max_color-min_color))*255
        
    ##########################
    
    return out_image



