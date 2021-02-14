def phase_amplitude(image):
    f = np.fft.fft2(image)
    amp=np.abs(f)
    phase=np.angle(f)
    return phase, amp

def draw_phase_amplitude(image):
    '''
    Returns the phase image and the amplitude image from the input image.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        tuple of numpy.ndarray: The tuple of the phase image and the amplitude image.   
    '''
    
    phase = image.copy()
    amp = image.copy()
    
    #Writer your code here
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    amp=20*np.log(np.abs(fshift))
    phase=np.angle(fshift)
  
    return phase, amp

def change_phase_domain(image1, image2):
    '''
    Substitutes the phase of image1 by the phase of image2 and returns two new images.
    
    Parameters:
        image1 (numpy.ndarray): The input image1.
        image2 (numpy.ndarray): The input image2.
    
    Returns:
        tuple of numpy.ndarray: The tuple of result images.   
    '''
    
    img1 = image1.copy()
    img2 = image2.copy()
    
    #Write your code here
    p1,a1=phase_amplitude(img1)
    p2,a2=phase_amplitude(img2)     
    img1=np.real(np.fft.ifft2(np.multiply(a2,np.exp(1j*p1))))
    img2=np.real(np.fft.ifft2(np.multiply(a1,np.exp(1j*p2))))
    
    return img1, img2

