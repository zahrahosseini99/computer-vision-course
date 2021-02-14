def hough_transform_line(image):
    '''
    Returns rho and theat of line detected and hough transform image.
    
    Parameters:
        image (numpy.ndarray): The input image.
        
    Returns:
        rho (float): Angle from origin to the line.
        theta (float): The distance from the origin to the line.
        hough_transform (numpy.ndarray): Hough transform image.
    '''

    img = image.copy()
    hough_transform = np.zeros_like(img)
    rho, theta = 0, 0

    #Write your code here
   
    # Rho and Theta ranges
    dtheta = 1
    drho = 1
    width, height = img.shape
    
    thetas =np.deg2rad(np.arange(-90,90,step=1))
    distance=int(np.sqrt(np.square(height) + np.square(width)))  
    rhos = np.arange(-distance, distance, step=drho)

    cos_thetas = np.cos(thetas)
    sin_thetas = np.sin(thetas)
    
    hough_transform = np.zeros((2*distance, len(thetas)))
    
    #edge detection
    edges = cv2.Canny(img, 20, 120)
    value_threshold =0
    are_edges = np.where(edges > value_threshold)
    y_idxs, x_idxs =are_edges
    
    #voting
    for i in range(len(x_idxs)):
        x = x_idxs[i]
        y = y_idxs[i]
        for t_idx in range(len(thetas)):
            rho = int(round(x * cos_thetas[t_idx] + y * sin_thetas[t_idx])+int(distance))
            hough_transform[rho][t_idx] += 1
            
    #Find the value(s) of rho,theta where hough_transform(rho,theta) is a large local maximum  
    max_value=np.argmax(hough_transform)
    x_max,y_max=np.unravel_index(max_value,hough_transform.shape)
    rho = x_max-distance
    theta = thetas[y_max]

    return rho, theta, hough_transform
    return rho, theta, hough_transform

