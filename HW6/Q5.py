import random
def non_zero_pixels(img):
    white_pixels=[]
    m,n=img.shape
    for i in range(m):
        for j in range(m):
            if img[i,j] != 0:
                white_pixels.append((np.float32(i),np.float32(j)))
    return white_pixels

def random_points(white_pixels):
    p1=0
    p2=0
    p1,p2 = random.sample(range(len(white_pixels)),2)
    point1, point2 = white_pixels[p1], white_pixels[p2]
    return point1, point2

def line_from_points(point1,point2):
    x1,y1=point1
    x2,y2=point2
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    return m,c

def distance(dots,m,c):
    threshold=1
    inlinear_points = []
    for d in dots:
        temp_x,temp_y=d
        distance = np.abs((m*temp_x+c)-temp_y)
        if distance < threshold:
            inlinear_points.append(d)        
    return len(inlinear_points), np.array(inlinear_points)
    

def car_to_pal(inlinear_points):
    x_bar=0
    y_bar=0
    xy_bar=0
    x2_bar=0
    y2_bar=0
    x_bar2=0
    y_bar2=0
    temp_x=0
    temp_y=0
    temp_xy=0
    count=len(inlinear_points)
    
    for i in range(count):
        x,y=inlinear_points[i]
        temp_x+=x
        temp_y+=y
        temp_xy+=x*y
    x_bar=temp_x/count
    y_bar=temp_y/count
    xy_bar=temp_xy/count
    
    square_inliers=np.square(inlinear_points)
    temp_x=0
    temp_y=0
    temp_xy=0
    for i in range(count):
        x,y=square_inliers[i]
        temp_x+=x
        temp_y+=y
    x2_bar=temp_x/count
    y2_bar=temp_x/count
    
    x_bar2, y_bar2 = np.square(x_bar), np.square(y_bar)
    
    theta = 0.5 * np.arctan((2*(xy_bar - x_bar*y_bar))/(x2_bar - y2_bar - x_bar2 + y_bar2))
    rho = x_bar * np.cos(theta) + y_bar*np.sin(theta)
    
    return rho, theta

def ransac(image):
    '''
    Gets input image and return rho and theta of line detected. 
    
    Parameters:
        image (numpy.ndarray): The input image.
        
    Returns:
        rho (float): The distance from the origin to the line.
        theta (float):  Angle from origin to the line.
    '''

    img = image.copy()
    rho, theta = 0, 0

    #Write your code here
    white_pixels=non_zero_pixels(img)
    max_inlier_points=-999999
    for i in range(20):
        point1,point2=random_points(white_pixels)
        m,c=line_from_points(point1,point2)
        count,inlinear_points=distance(white_pixels,m,c)
        if count>max_inlier_points:
            max_inlier_points=count
            max_inliers=inlinear_points
    

    rho,theta=car_to_pal(max_inliers)

    return rho, theta

