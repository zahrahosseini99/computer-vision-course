def AR(background, image):
    '''
    Adds the input image to the background image properly.
    
    Parameters:
        background (numpy.ndarray) : background image
        image (numpy.ndarray): input image
    
    Returns:
        numpy.ndarray: The result image.
    '''
    
    out_img = background.copy()

    #Write your code here
    pts1 = np.float32([[235,233],[146,224],[150,109],[233,106]])
    pts2 = np.float32([[1199,1799],[0,1799],[0,0],[1199,0]])
    M, mask = cv2.findHomography(pts2, pts1)
    
    masked_img = cv2.warpPerspective(image, M, (background.shape[1],background.shape[0]))

    
    for i in range(background.shape[0]):
        for j in range(background.shape[1]):
            for k in range(background.shape[2]):
                if masked_img[i,j,k]>0:
                     out_img[i,j,k]=masked_img[i,j,k]

    return out_img

