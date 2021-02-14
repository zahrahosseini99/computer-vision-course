def opening(img,element):
    eroded=cv2.erode(img,element)
    opened=cv2.dilate(eroded,element)
    return opened    

def get_skeleton(image):
    """
    Finds the skeleton of the input image.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The skeleton image.  
    """
    
    img = image.copy()
    
    #Write your code here
    
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
    img_smoothed = cv2.GaussianBlur(np.float32(img),(7,7),0)
    ret,img_thereshold = cv2.threshold(np.float32(img_smoothed),230,255,cv2.THRESH_BINARY_INV)
    image=np.uint8(img_thereshold.copy())
    result = np.zeros(img.shape, np.uint8)
    
    while True:
        eroded=cv2.erode(image,element)
        opened=opening(eroded,element)
        temp=cv2.subtract(eroded,opened)
        result=cv2.bitwise_or(result,temp)
        image=np.uint8(eroded.copy())
        if cv2.countNonZero(image)==0:
            break
    
    return result

