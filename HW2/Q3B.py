def histogram_equalization(image):
    '''
    Equalizes the histogram of the input image.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The result image that it's histogram be eqaulized.   
    '''
    
    h = compute_histogram(image)
    out_image = image.copy()

    ####### your code ########
    cdf=[None]*256
    s=0
    temp=0
    m,n=image.shape
    size=n*m
    for i in range(0,256):
      s+=h[i]
      cdf[i]=round(255*(s/199108))
    for i in range(m):
            for j in range(n):
              out_image[i,j]=cdf[image[i,j]]
                
    ##########################
        
    return out_image  



