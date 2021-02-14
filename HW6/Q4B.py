def detect_lines_hough(image):
    '''
    Returns the image which lines have been detected.
    
    Parameters:
        image (numpy.ndarray): The input image.
        
    Returns:
        out_img (numpy.ndarray): The result image.
    '''
    out_img = image.copy()
    
    #Writer your code here
    gray = cv2.cvtColor(out_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(3,3),1)
    edges = cv2.Canny(gray,20,100)
    lines=np.array([])
    
    #The other parameter rho=0.1 defines how fat a row of the accumulator is.
    #Output vector of lines. Each line is represented by a 4 element vector (x1,y1,x2,y2) , where (x1,y1) and (x2,y2) are the
    #Angle resolution of the accumulator in radians
    lines = cv2.HoughLinesP(edges, 0.1, np.pi / 180, 1, lines)
    
    white=(255,255,255)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(out_img,(x1,y1),(x2,y2),white,2) #draw white lines


    return out_img

