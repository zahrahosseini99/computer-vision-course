def get_dif(image1, image2):
    '''
    Creates a new image that differences between two input images are shown.
    
    Parameters:
        image1 (numpy.ndarray): The first input image.
        image2 (numpy.ndarray): The second input image.
    
    Returns:
        numpy.ndarray: The result difference image.
    '''
    
    out_img = image1.copy()
    
    #Write your code here
    # convert to 3 equal channels
    out_img = cv2.merge((out_img, out_img, out_img))
    for i in range(image1.shape[0]):
        for j in range(image1.shape[1]):
            out_img[i,j]=out_img[i,j]*[1,0,0]
            
    out_img2 = image2.copy()
    out_img2 = cv2.merge((out_img2, out_img2, out_img2))
    for i in range(image2.shape[0]):
        for j in range(image2.shape[1]):
            out_img2[i,j]=out_img2[i,j]*[0,1,1]
            
    result= out_img2+out_img       
    return result

