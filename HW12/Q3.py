import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, exposure
from tqdm import tqdm
from sklearn import svm
from skimage import color

def classify_hog(x_train, y_train, x_test):
    '''
    Classifies images with HOG.
    
    Parameters:
        x_train(numpy.ndarray) : train data
        y_train(numpy.ndarray) : train labels
        x_test(numpy.ndarray) : test data
        
    outputs:
        predicted_labels(numpy.ndarray): labels that predicted
    '''
    
    x_t = x_train.copy()
    y_t = y_train.copy()
    x_te = x_test.copy()
    predicted_labels = None
    
    #Write your code here
    x_test = [ color.rgb2gray(i) for i in x_te]
    ppc = 8
    hog_images_train = []
    hog_features_train = []
    
    for image in tqdm(x_train):
        fd,hog_image = hog(image, orientations=8, pixels_per_cell=(ppc,ppc),cells_per_block=(3, 3),block_norm= 'L2',visualize=True)
        hog_images_train.append(hog_image)
        hog_features_train.append(fd)
        
    hog_images = []
    hog_features = []
    
    for image in tqdm(x_test):
        fd,hog_image = hog(image, orientations=8, pixels_per_cell=(ppc,ppc),cells_per_block=(3, 3),block_norm= 'L2',visualize=True)
        hog_images.append(hog_image)
        hog_features.append(fd)     

    clf = LinearSVC()
    clf.fit(hog_features_train,y_train)
    y_pred = clf.predict(hog_features)
    return y_pred    

def find_greater_contour(countors):
    inx=-1
    maxVal=-999999
    i=0
    for i in range(len(countors)):
        area = cv2.contourArea(countors[i])
        if area>maxVal:
            maxVal=area
            inx=i
    return inx

def classify_shape_desc(x_train, y_train, x_test):
    '''
    Classifies images by using shape descriptors.
    
    Parameters:
        x_train(numpy.ndarray) : train data
        y_train(numpy.ndarray) : train labels
        x_test(numpy.ndarray) : test data
        
    outputs:
        predicted_labels(numpy.ndarray): labels that predicted
    '''
    
    x_t = x_train.copy()
    y_t = y_train.copy()
    x_te = x_test.copy()
    predicted_labels = None
    
    #Write your code here
    images_train = []
    
    for image in tqdm(x_train):
        ret, thresh = cv2.threshold(image, 10,255, 0)
        contours, _ = cv2.findContours(thresh,1,1)
        inx=find_greater_contour(contours)
        ellipse=cv2.fitEllipse(contours[inx])
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
        images_train.append([ecc,solidity,aspect_ratio])
        
    images_test = []
    
    for image in tqdm(x_test):
        ret, thresh = cv2.threshold(image, 10, 255, 0)
        contours, _ = cv2.findContours(thresh,1,1)
        inx=find_greater_contour(contours)
        ellipse=cv2.fitEllipse(contours[inx])
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
        images_test.append([ecc,solidity,aspect_ratio])

    clf = LinearSVC()
    clf.fit(images_train,y_train)
    y_pred = clf.predict(images_test)
    
    return y_pred   

def myLBP(img):
    '''
    Extracts LBP features from the input image.
    
    Parameters:
        img(numpy.ndarray) : image data
    outputs:
        output: LBP features
    '''
    
    input_img = img.copy()
    output = None
    
    #Write your code here
    
    output=np.zeros((26, 26))
    temp = img.copy()
    win_size=3
    size=win_size//2
    power_val = np.matrix([[1, 2, 4], [128, 0,8],[64,32,16]])
    r,c=img.shape
    for i in range(1,r-1):
        for j in range(1,c-1):
            temp=np.zeros((3,3))
            sliced=img[i-1:i+2,j-1:j+2]
            ones=np.where(sliced>sliced[1,1])
            zeros=np.where(sliced<=sliced[1,1])
            temp[ones]=1
            temp[zeros]=0
            output[i-1,j-1]= np.sum(np.multiply(power_val,temp))  

            
           
    return output

def classify_your_lbp(x_train, y_train, x_test):
    '''
    Classifies images by using your LBP.
    
    Parameters:
        x_train(numpy.ndarray) : train data
        y_train(numpy.ndarray) : train labels
        x_test(numpy.ndarray) : test data
        
    outputs:
        predicted_labels(numpy.ndarray): labels that predicted
    '''
    
    x_t = x_train.copy()
    y_t = y_train.copy()
    x_te = x_test.copy()
    predicted_labels = None
    
    #Write your code here
    images_train = []
    features_train = []
    
    for image in tqdm(x_train):
        lbp_temp=myLBP(image)
        hist, _ = np.histogram(lbp_temp, density=True, bins=256, range=(0, 256))
        images_train.append(hist)
        
    images_test = []
    features_test = []
    
    for image in tqdm(x_test):
        lbp_temp=myLBP(image)
        hist, _ = np.histogram(lbp_temp, density=True, bins=256, range=(0, 256))
        images_test.append(hist)
            
            
    clf = LinearSVC()
    clf.fit(images_train,y_train)
    y_pred = clf.predict(images_test)

    return y_pred    

def classify_skimage_lbp(x_train, y_train, x_test):
    '''
    Classifies images by using Scikit-Image LBP.
    
    Parameters:
        x_train(numpy.ndarray) : train data
        y_train(numpy.ndarray) : train labels
        x_test(numpy.ndarray) : test data
        
    outputs:
        predicted_labels(numpy.ndarray): labels that predicted
    '''
    
    x_t = x_train.copy()
    y_t = y_train.copy()
    x_te = x_test.copy()
    predicted_labels = None
    
    #Write your code here
    P = 8
    R = 1
    images_train = []
    features_train = []
    
    for image in tqdm(x_train):
        lbp = ft.local_binary_pattern(image, P, R)
        hist, _ = np.histogram(lbp, density=True, bins=256, range=(0, 256))
        images_train.append(hist)
        
    images_test = []
    features_test = []
    
    for image in tqdm(x_test):
        lbp = ft.local_binary_pattern(image, P, R)
        hist, _ = np.histogram(lbp, density=True, bins=256, range=(0, 256))
        images_test.append(hist)
            
    clf = LinearSVC()
    clf.fit(images_train,y_train)
    y_pred = clf.predict(images_test)
    
    return y_pred    

