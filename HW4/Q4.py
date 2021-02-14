def denoise_image(image):
    '''
    Denoises the input image.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The result denoised image.   
    '''
    
    denoised = image.copy()
    
    #Write your code here
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    amp=np.log(np.abs(fshift))
    m,n=image.shape
    #print(m,n)
    for i in range(0,206):
        for j in range(0,512):
            fshift[i,j]=0
            fshift[j,i]=0
    for i in range(306,512):
        for j in range(0,512):
            fshift[i,j]=0
            fshift[j,i]=0
            

    denoised=np.real(np.fft.ifft2(np.fft.ifftshift(fshift)))

    return denoised

