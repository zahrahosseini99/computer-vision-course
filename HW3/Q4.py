def mapping(image):
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
      cdf[i]=round(255*(s/size))
    
    ##########################
        
    return cdf 

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

def histogram_matching(img, ref_img):
    '''
    Matchs the histogram of the input image to the histogram of reference image.
    
    Parameters:
        img (numpy.ndarray): The input image.
        ref_img (numpy.ndarray): The reference image.
    
    Returns:
        numpy.ndarray: The result image.
    '''
    
    out_img = img.copy()
    
    ####### your code ########
    n,m=img.shape
    T_img=mapping(img)
    T_ref_img=mapping(ref_img)
    
    res=[None]*256
    for i in range(256):
        for j in range(256):
            if T_img[i]==T_ref_img[j]:
                res[i]=j

        
    for i in range(256):
        if res[i]==None:
            tmp=T_ref_img.copy()
            tmp = [abs(x - T_img[i]) for x in tmp]
            x=min(tmp)
            index = tmp.index(x)
            res[i]=index
   
    for i in range(n):
        for j in range(m):
            out_img[i,j]=res[img[i,j]]
    ##########################
    
    return out_img

