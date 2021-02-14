def filter_corners(corners,image):
    corners = cv2.dilate(corners, None)
    max_corner_value=corners.max()
    indexex = np.where(corners > 0.04 * max_corner_value)
    filtered_points=np.zeros((image.shape[0],image.shape[1]))
    filtered_points[indexex]=1
    return filtered_points

def find_and_filter_keypoints(image):
    corners = cv2.cornerHarris(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY), 3, 3, 0.1)
    best_corners=filter_corners(corners,image)
    return best_corners

def checking(keypoints,h,w,discriptor_size,threshold,i,j):
    if keypoints[i, j]:
            if i + discriptor_size >= h or j + discriptor_size >= w or i -discriptor_size < 0 or j - discriptor_size < 0:
                keypoints[i, j] = 0
            else:
                keypoints[i - threshold:i + threshold + 1, j -threshold:j + threshold + 1] = 0
                keypoints[i, j] = 1
    return keypoints

def double_filtering_keypoints(keypoints_image1,keypoints_image2,threshold, discriptor_size):
    
    h, w = keypoints_image1.shape
    
    discriptor_size=discriptor_size//2
    threshold=threshold//2
    for i in range(h):
        for j in range(w):
            keypoints_image1=checking(keypoints_image1,h,w,discriptor_size,threshold,i,j)
                    
    h, w=keypoints_image2.shape
    for i in range(h):
        for j in range(w):
            keypoints_image2=checking(keypoints_image2,h,w,discriptor_size,threshold,i,j)
                        
    return keypoints_image1,keypoints_image2

def compare_windows(image1, keypoints_image1, image2, keypoints_image2, disc_size):
    x = disc_size // 2
    scores_list = []
    for s in keypoints_image1:
        temp = -1
        best_score = 0
        for d in keypoints_image2:
            windows1 = image1[s[0] - x:s[0] + x + 1, s[1] - x:s[1] + x + 1, :]
            windows2 = image2[d[0] - x:d[0] + x + 1, d[1] - x:d[1] + x + 1, :]
            sc = cv2.matchTemplate(windows1, windows2, cv2.TM_CCORR_NORMED)
            if sc > temp:
                temp = sc
                best_score = d
        scores_list.append(best_score)
    return scores_list

def indexing(keypoints):
    indexes=list()
    for i in range(keypoints.shape[0]):
        for j in range(keypoints.shape[1]):
            if keypoints[i,j]==1:
                indexes.append(tuple((i,j)))
    return indexes

def draw_lines(srcs, dsts, image, image2):
    resizer=image2.shape[1]
    for src_point, tar_point in zip(srcs, dsts):
        src_inverted = (src_point[1], src_point[0])
        tar_inverted = (tar_point[1] + resizer, tar_point[0])
        cv2.line(image, src_inverted, tar_inverted, (np.random.randint(0, 255),
                                                     np.random.randint(0, 255), np.random.randint(0, 255)), 2)
    return image

def find_match(image1, image2):
    '''
    Finds match points between two input images.
    
    Parameters:
        image1 (numpy.ndarray): input image.
        image2 (numpy.ndarray): second input image.
    
    Returns:
        numpy.ndarray: The result image.
    '''
    
    result = None
    
    #Write your code here
    threshold = 11
    discriptor_size = 15
    keypoints_image1 = find_and_filter_keypoints(image1)
    keypoints_image2 = find_and_filter_keypoints(image2)

    keypoints_image1,keypoints_image2=double_filtering_keypoints(keypoints_image1,keypoints_image2,threshold, discriptor_size)
    
    keypoints_image1 = indexing(keypoints_image1)
    keypoints_image2 = indexing(keypoints_image2)
    rslt = compare_windows(image1, keypoints_image1, image2, keypoints_image2,discriptor_size)
    f = np.concatenate([image1, image2], axis = -2)
    result = draw_lines(keypoints_image1, rslt, f, image2)



    return result

