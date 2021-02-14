def remove_circles(image):
    '''
    Returns the image which circles have been removed.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        out_img (numpy.ndarray): The result image.
    '''
    out_img = image.copy()
    

    #Writer your code here
    gray = cv2.cvtColor(out_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(3,3),1)
    detected_circles = cv2.HoughCircles(gray,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 100)
    for x, y, r in detected_circles[0]:
        cv2.circle(out_img, (x,y), int(r+3), 0, -1)  #r +/- <4  
    return out_img

