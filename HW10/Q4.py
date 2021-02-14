structuring_element = np.ones((40,40))

def your_dilate(image, structuring_element):
    '''
    Applies your dilation.
    
    Parameters:
        image (numpy.ndarray): The input image.
        structuring_element (numpy.ndarray): The structuring element must be square.
    
    Returns:
        numpy.ndarray: The result image.
    '''
    
    result = image.copy()
    
    #Write your code here
    
    result=cv2.filter2D(image,-1,structuring_element,cv2.BORDER_CONSTANT)
    indx=np.where(result>=1)
    result[indx]=1
    
    return result

def your_erode(image, structuring_element):
    '''
    Applies your erosion.
    
    Parameters:
        image (numpy.ndarray): The input image.
        structuring_element (numpy.ndarray): The structuring element must be square.
    
    Returns:
        numpy.ndarray: The result image.
    '''
    
    result = image.copy()
    
    #Write your code here
    stSums=np.sum(structuring_element)
    result=np.float32(result)//255
    result=cv2.filter2D(result,-1,structuring_element,cv2.BORDER_CONSTANT)
    greaterIndx=np.where(result>=stSums)
    lowerIndx=np.where(result<stSums)
    result[greaterIndx]=1
    result[lowerIndx]=0
    
    return result

def cv_dilate(image, structuring_element):
    '''
    Applies OpenCV dilation.
    
    Parameters:
        image (numpy.ndarray): The input image.
        structuring_element (numpy.ndarray): The structuring element must be square.
    
    Returns:
        numpy.ndarray: The result image.
    '''
    
    result = image.copy()
    
    #Write your code here
    result=cv2.dilate(image,structuring_element)
    
    
    return result

def cv_erode(image, structuring_element):
    '''
    Applys OpenCV erosion.
    
    Parameters:
        image (numpy.ndarray): The input image.
        structuring_element (numpy.ndarray): The structuring element must be square.
    
    Returns:
        numpy.ndarray: The result image.
    '''
    
    result = image.copy()
    
    #Write your code here
    result=cv2.erode(image,structuring_element)
    
    
    return result

