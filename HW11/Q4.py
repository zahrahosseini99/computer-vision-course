structuring_element = np.ones((5,5))

def RGB_dilate(image, structuring_element):
    '''
    Applies dilation in RGB space.
    
    Parameters:
        image (numpy.ndarray): The input image.
        structuring_element (numpy.ndarray): The structuring element must be square.
    
    Returns:
        dilated_image (numpy.ndarray): The dilated result image.   
    '''

    img = image.copy()
    dilated_image = image.copy()
    
    #Write your code here
    size=structuring_element.shape[0]//2
    image = cv2.copyMakeBorder(image,top=size,bottom=size,left=size,right=size,borderType=cv2.BORDER_REPLICATE)
    image1 = cv2.copyMakeBorder(img,top=size,bottom=size,left=size,right=size,borderType=cv2.BORDER_REPLICATE)
    R=image1[:,:,0]
    G=image1[:,:,1]
    B=image1[:,:,2]
    for i in range(size,image.shape[0]-size):
        for j in range(size,image.shape[1]-size):
            R[i,j]=np.max(image[i-size:i+size+1,j-size:j+size+1,0])
            G[i,j]=np.max(image[i-size:i+size+1,j-size:j+size+1,1])
            B[i,j]=np.max(image[i-size:i+size+1,j-size:j+size+1,2])
            #print(image[i-size:i+size+1,j-size:j+size+1])
            #print(image[i-size:i+size+1,j-size:j+size+1].shape)
    
    dilated_image=cv2.merge([R,G,B])
    return dilated_image[size:-size,size:-size,:]

def RGB_erode(image, structuring_element):
    '''
    Applies erosion in RGB space.
    
    Parameters:
        image (numpy.ndarray): The input image.
        structuring_element (numpy.ndarray): The structuring element must be square.
    
    Returns:
        eroded_image (numpy.ndarray): The eroded result image.   
    '''
    
    img = image.copy()
    eroded_image = image.copy()
    
    #Write your code here
    size=structuring_element.shape[0]//2
    image = cv2.copyMakeBorder(image,top=size,bottom=size,left=size,right=size,borderType=cv2.BORDER_REPLICATE)
    image1 = cv2.copyMakeBorder(img,top=size,bottom=size,left=size,right=size,borderType=cv2.BORDER_REPLICATE)
    R=image1[:,:,0]
    G=image1[:,:,1]
    B=image1[:,:,2]
    for i in range(size,image.shape[0]-size):
        for j in range(size,image.shape[1]-size):
            R[i,j]=np.min(image[i-size:i+size+1,j-size:j+size+1,0])
            G[i,j]=np.min(image[i-size:i+size+1,j-size:j+size+1,1])
            B[i,j]=np.min(image[i-size:i+size+1,j-size:j+size+1,2])
    eroded_image=cv2.merge([R,G,B])
    return eroded_image[size:-size,size:-size,:]

