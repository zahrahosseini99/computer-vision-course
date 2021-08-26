def classify_leaf(image):
    '''
    Classifies the input image to only two classes of leaves.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        int: The class of the image. 1 == apple, 0 == linden
    '''
    
    leaf_type = 0
    
    #Write your code here
    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(img_gray,(3,3),0)
    ret, thresh = cv2.threshold(blur, 220, 255, 0)
    
    contours, _ = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )
    inx=find_greater_contour(contours)
    

    (x,y), (MA,ma), angle = cv2.fitEllipse(contours[inx])
    a=ma / 2
    b=MA /2
    ecc=np.sqrt(a**2 - b**2) / a

    area = cv2.contourArea(contours[inx])
    hull = cv2.convexHull(contours[inx])
    hull_area = cv2.contourArea(hull)
    solidity = float(area)/hull_area

    x,y,w,h = cv2.boundingRect(contours[inx])
    aspect_ratio = float(w)/h

    area = cv2.contourArea(contours[inx])
    x,y,w,h = cv2.boundingRect(contours[inx])
    rect_area = w*h
    extent = float(area)/rect_area
    
    if solidity == 1:
        if aspect_ratio <0.7 and ecc <0.9:
            if extent > 0.9959:
                return 0
        if ecc <0.5:
            return 0
        else:
            return 1

    return leaf_type

