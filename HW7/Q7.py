def gradient_x(img):
    ##Sobel operator kernels
    kernel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    return cv2.filter2D(img,-1,kernel_x)

def gradient_y(img):
    ##Sobel operator kernels
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    return cv2.filter2D(img,-1,kernel_y)

def gaussian_kernel(size, sigma=1):
    gaussian = None
    gaussian = np.zeros((size,size), np.float)
    coe=1/(2*((np.pi)*(sigma**2)))
    co2_std=2*(sigma**2)
    for i in range(size):
        for j in range(size):
            gaussian[i,j]+=(coe*np.exp((-(i**2+j**2)/co2_std)))
    return gaussian


def harris_points(image):
    '''
    Gets corner points by applying the harris detection algorithm.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The result image.
    '''
    
    out_img = image.copy()
    
    #Write your code here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    I_x = gradient_x(np.float32(gray))
    I_y = gradient_y(np.float32(gray))
    kernel_size=3
    sigma=1
    kernel=gaussian_kernel(kernel_size,sigma)
    img_smoothed = cv2.filter2D(np.float32(image),-1,np.float32(kernel))
    
    Ixx = cv2.filter2D(np.float32(I_x**2),-1,np.float32(kernel))
    Ixy = cv2.filter2D(np.float32(I_y*I_x),-1,np.float32(kernel))
    Iyy = cv2.filter2D(np.float32(I_y**2),-1,np.float32(kernel))
    
    k=0.05
    
    # determinant
    detA = Ixx * Iyy - Ixy ** 2
    # trace
    traceA = Ixx + Iyy
    
    harris_response = detA - k * (traceA ** 2)

    max_val=np.argmax(harris_response)/10
    for rowindex, response in enumerate(harris_response):
        for colindex, r in enumerate(response):
            if r > max_val:
                # this is a corner
                cv2.circle(out_img,(rowindex, colindex),2,(255,0,0), -1)

    return out_img

