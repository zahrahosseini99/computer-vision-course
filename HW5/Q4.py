def get_45_edges(image):
    '''
    Returns the image which shows the 45-degree edges.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        edges_45 (numpy.ndarray): The 45-degree edges of input image.
    '''
    kernel = None
    edges_45 = image.copy()
    
    #Writer your code here
    kernel=np.array([[2,1,0],[1,0,-1],[0,-1,-2]],np.float)
    edges_45=cv2.filter2D(image,-1,np.float32(kernel))
    return edges_45

def get_135_edges(image):
    '''
    Returns the image which shows the 135-degree edges.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        edges_135 (numpy.ndarray): The 135-degree edges of input image.
    '''
    kernel = None
    edges_135 = image.copy()
    #Writer your code here
    kernel=np.array([[0,-1,-2],[1,0,-1],[2,1,0]],np.float)
    edges_135=cv2.filter2D(image,-1,np.float32(kernel))
    
    return edges_135

