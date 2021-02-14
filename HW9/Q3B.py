def local_otsu(image):
    '''
    Applys local otsu on the input image.
    
    Parameters:
        image (numpy.ndarray): The input image.
    
    Returns:
        numpy.ndarray: The result panorama image.
    '''
    
    out_img = image.copy()
    
    #Write your code here

    half_rows=image.shape[0]//2
    half_cols=image.shape[1]//2
    out_img[:half_rows, :half_cols] = global_otsu(image[:half_rows, :half_cols])
    out_img[:half_rows, half_cols:] = global_otsu(image[:half_rows, half_cols:])
    out_img[half_rows:, :half_cols] = global_otsu(image[half_rows:, :half_cols])
    out_img[half_rows:, half_cols:] = global_otsu(image[half_rows:, half_cols:])
    
    return out_img

