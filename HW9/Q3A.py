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

def global_otsu(image):
    '''
    Applys global otsu on the input image.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The result panorama image.
    '''



   

    
    out_img = image.copy()
    
       
    
    #Write your code here
    final_value = 99999999
    final_thresh = 0
    histogram = compute_histogram(image)
    pixel_count = np.sum(histogram)
    for t in range(1, 255):
        W1 = np.sum(histogram[:t])/pixel_count
        W2 = np.sum(histogram[t:])/pixel_count
        V1 = np.var(image[image < t])
        V2 = np.var(image[image >= t])
        value = W1 * V1 + W2 * V2
        if value < final_value:
            final_value = value
            final_thresh = t
    final_img = image.copy()
    out_img[final_img > final_thresh] = 255
    out_img[final_img < final_thresh] = 0
    
    return out_img

