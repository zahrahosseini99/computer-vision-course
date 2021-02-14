def distance(point1,point2):
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def butterworthHP(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1-1/(1+(distance((y,x),center)/D0)**(2*n))
    return base

def enhance_image(image):
    '''
    Enhances the input image by applying a filter in the frequency domain.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The result enhanced image.   
    '''
    
    enhanced = image.copy()
    
    #Write your code here
    r,c = image.shape
    #Write your code her
    original = np.fft.fft2(image)
    center = np.fft.fftshift(original)
    HighPassCenter = center * butterworthHP(20,image.shape,10)
    HighPass = np.fft.ifftshift(HighPassCenter)
    inverse_HighPass = np.fft.ifft2(HighPass)
    enhanced = np.array(enhanced,np.float64) + np.abs(inverse_HighPass)
    return enhanced

