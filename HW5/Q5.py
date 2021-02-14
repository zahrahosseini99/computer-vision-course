def gaussian_kernel(size, sigma=1):
    '''
    Calculates and Returns Gaussian kernel.

    Parameters:
        size (int): size of kernel.
        sigma(float): standard deviation of gaussian kernel

    Returns:
        gaussian: A 2d array shows gaussian kernel
    '''
    #Writer your code here
    gaussian = None
    gaussian = np.zeros((size,size), np.float)
    
    ####### your code ########
    coe=1/(2*((np.pi)*(sigma**2)))
    co2_std=2*(sigma**2)
    for i in range(size):
        for j in range(size):
            gaussian[i,j]+=(coe*np.exp((-(i**2+j**2)/co2_std)))

    return gaussian

def sobel_filters(image):
    '''
    finds the magnitude and orientation of the image using Sobel kernels.

    Parameters:
        image (numpy.ndarray): The input image.

    Returns:
        (magnitude, theta): A tuple consists of magnitude and orientation of the image gradients.
    '''
    #Writer your code here
    
    
    ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float)
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float)
    Ix = cv2.filter2D(np.float32(image),-1,np.float32(kx))
    Iy = cv2.filter2D(np.float32(image),-1,np.float32(ky))
            
    magnitude = np.hypot(Ix, Iy) #Result is equivalent to Equivalent to sqrt(x1**2 + x2**2), element-wise
    magnitude = magnitude / magnitude.max() * 255
    theta = np.arctan2(Iy, Ix)
    
    return magnitude, theta

def non_max_suppression(image, theta): 
    '''
    Applies Non-Maximum Suppression.

    Parameters:
        image (numpy.ndarray): The input image.
        theta (numpy.ndarray): The orientation of the image gradients.

    Returns:
        Z(numpy.ndarray): Output of Non-Maximum Suppression algorithm.
    '''
    #Writer your code here
    M, N = image.shape
    Z = np.zeros((M,N), np.float)
    angle = theta * 180. / np.pi
    angle[angle < 0] += 180 ## becuse of that -180,180 +180 to become between 0,360

    
    for i in range(1,M-1):
        for j in range(1,N-1):
                t1=255
                t2 = 255
                if (0 <= angle[i,j] < 22.5):
                    t1 = image[i, j+1]
                    t2 = image[i, j-1]
                elif (157.5 <= angle[i,j] <= 180):
                    t1 = image[i, j+1]
                    t2 = image[i, j-1]
                elif (22.5 <= angle[i,j] < 67.5):
                    t1 = image[i+1, j-1]
                    t2 = image[i-1, j+1]
                elif (67.5 <= angle[i,j] < 112.5):
                    t1 = image[i+1, j]
                    t2 = image[i-1, j]
                elif (112.5 <= angle[i,j] < 157.5):
                    t1 = image[i-1, j-1]
                    t2 = image[i+1, j+1]
                if (image[i,j] >= t1) and (image[i,j] >= t2):
                    Z[i,j] = image[i,j]
                else:
                    Z[i,j] = 0

    return Z
#Non-Max Suppression step will help us mitigate the thick ones.

def hysteresis_threshold(image, lowThreshold=38, highThreshold=70):
    '''
    Finds strong, weak, and non-relevant pixels.

    Parameters:
        image (numpy.ndarray): The input image.
        lowThreshold(int): Low Threshold.
        highThreshold(int): High Threshold.
        
    Returns:
        result(numpy.ndarray): Output of applying hysteresis threshold.
    '''
    #Writer your code here
    M, N = image.shape
    result = np.zeros((M,N), dtype=np.int32)  
    
    weak = np.int32(20)
    strong = np.int32(255)
    
    higher1, higher2 = np.where(image >= highThreshold)    
    middle1, middle2 = np.where((image <= highThreshold) & (image >= lowThreshold))
    
    result[higher1, higher2] = strong
    result[middle1, middle2] = weak
    
    final=result.copy()
    
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (result[i,j] == weak):
                    if (result[i+1, j-1] == strong):
                        final[i, j] = strong
                    elif (result[i+1, j] == strong):
                        final[i, j] = strong
                    elif (result[i+1, j+1] == strong):
                        final[i, j] = strong
                    elif (result[i, j-1] == strong):
                        final[i, j] = strong
                    elif (result[i, j+1] == strong):
                        final[i, j] = strong
                    elif (result[i-1, j-1] == strong):
                        final[i, j] = strong
                    elif (result[i-1, j] == strong):
                        final[i, j] = strong
                    elif (result[i-1, j+1] == strong):
                        final[i, j] = strong
                    else:
                        final[i, j] = 0
    
    return result,final


def canny(image, kernel_size = 3, sigma = 1, lowtreshold = 38, hightreshold =70):
    '''
    Applys Canny edge detector on the input image.

    Parameters:
        image (numpy.ndarray): The input image.
        size (int): size of kernel.
        sigma(float): standard deviation of gaussian kernel.
        lowThreshold(int): Low Threshold.
        highThreshold(int): High Threshold.
        
    Returns:
        img_smoothed(numpy.ndarray): Result of applying the Gaussian kernel on the input image.
        gradient(numpy.ndarray): The image of the gradients.
        nonMaxImg(numpy.ndarray): Output of Non-Maximum Suppression algorithm.
        thresholdImg(numpy.ndarray): Output of applying hysteresis threshold.
        img_final(numpy.ndarray): Result of canny edge detector. The image of detected edges.
    '''
    kernel=gaussian_kernel(kernel_size,sigma)
    img_smoothed = cv2.filter2D(np.float32(image),-1,np.float32(kernel))
    gradient,theta = sobel_filters(image)
    nonMaxImg = non_max_suppression(gradient,theta)
    thresholdImg,img_final = hysteresis_threshold(nonMaxImg,lowtreshold,hightreshold)

    return img_smoothed, gradient, nonMaxImg, thresholdImg, img_final

