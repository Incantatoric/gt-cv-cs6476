import cv2
import numpy as np
from matplotlib import pyplot as plt
import itertools


def traffic_light_detection(img_in, radii_range):
    """Finds the coordinates of a traffic light image given a radii
    range.
    Use the radii range to find the circles in the traffic light and
    identify which of them represents the yellow light.
    Analyze the states of all three lights and determine whether the
    traffic light is red, yellow, or green. This will be referred to
    as the 'state'.
    It is recommended you use Hough tools to find these circles in
    the image.
    The input image may be just the traffic light with a white
    background or a larger image of a scene containing a traffic
    light.
    Args:
        img_in (numpy.array): image containing a traffic light.
        radii_range (list): range of radii values to search for.
    Returns:
        tuple: 2-element tuple containing:
        coordinates (tuple): traffic light center using the (x, y)
                             convention.
        state (str): traffic light state. A value in {'red', 'yellow',
                     'green'}
    """

    gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # 2. Find Circles
    min_r = min(radii_range)
    max_r = max(radii_range)

    circles = cv2.HoughCircles(
        gray_blurred,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=min_r * 2,
        param1=100,
        param2=5,  
        minRadius=min_r,
        maxRadius=max_r
    )

    if circles is None:
        return (0, 0), "red"

    circles = np.uint16(np.around(circles[0, :]))

    if len(circles) < 3:
        return (0, 0), "red"

    # Find the triplet.
    best_triplet = []
    best_score = float('inf') 

    for triplet_raw in itertools.combinations(circles, 3):
        
        triplet = sorted(triplet_raw, key=lambda c: c[1])

        xs = [c[0] for c in triplet]
        
        ys = [int(c[1]) for c in triplet] 
        rs = [c[2] for c in triplet]
        
        x_std = np.std(xs)
        avg_r = np.mean(rs)
        
        if x_std > (avg_r * 0.75): 
            continue 
            
        r_std = np.std(rs)
        
        if r_std > (avg_r * 0.5):
            continue

        dist1 = ys[1] - ys[0]
        dist2 = ys[2] - ys[1]
        
        if dist1 < (avg_r) or dist2 < (avg_r):
             continue
        
        spacing_ratio = dist1 / (dist2 + 1e-6) # Add epsilon to avoid divide by zero.
        if spacing_ratio < 0.5 or spacing_ratio > 2.0:
             continue
        
        score = x_std + r_std + abs(dist1 - dist2) 
        
        if score < best_score:
            best_score = score
            best_triplet = triplet
            
    if not best_triplet:
        return (0, 0), "red"
        
    found_lights = best_triplet
    
    # Identify Center (Yellow Light).
    top_light = found_lights[0]
    middle_light = found_lights[1]
    bottom_light = found_lights[2]
    
    coordinates = (int(middle_light[0]), int(middle_light[1]))

    # State.
    hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)
    
    c_top = hsv[int(top_light[1]), int(top_light[0])]
    c_mid = hsv[int(middle_light[1]), int(middle_light[0])]
    c_bot = hsv[int(bottom_light[1]), int(bottom_light[0])]

    values = [c_top[2], c_mid[2], c_bot[2]]
    brightest_idx = np.argmax(values)
    
    if brightest_idx == 0:
        state = 'red'
    elif brightest_idx == 1:
        state = 'yellow'
    else:
        state = 'green'
            
    return coordinates, state

def construction_sign_detection(img_in):
    """Finds the centroid coordinates of a construction sign in the
    provided image.
    Args:
        img_in (numpy.array): image containing a traffic light.
    Returns:
        (x,y) tuple of the coordinates of the center of the sign.
    """
    
    # Convert to HSV to isolate the orange color.
    hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)
    
    # Hue: ~10-25, Saturation & Value: high to avoid brown/dark colors (I guess?)
    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([25, 255, 255])
    
    # Create a binary mask of orange pixels.
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Use Canny edge detector on the mask to get the sign's outline
    edges = cv2.Canny(mask, 50, 150)

    # Find Lines using HoughLinesP.
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=20,       # Minimum number of votes.
        minLineLength=20,   # Minimum length in pixels.
        maxLineGap=10       # Max gap to connect segments.
    )

    if lines is None:
        return (0, 0) # No lines found

    # The sign is an upright diamond, so its edges are at ~45 and ~135 deg.
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    valid_line_found = False
    for line in lines:
        x1, y1, x2, y2 = line[0]
        
        # Avoid division by zero.
        if (x2 - x1) == 0:
            continue
        
        # Calculate angle in degrees.
        angle_rad = np.arctan((y2 - y1) / (x2 - x1))
        angle_deg = np.degrees(angle_rad)

        # Check if angle is ~45 deg or ~135 deg (-45 deg).
        # We give a tolerance here.
        if (30 < abs(angle_deg) < 60):
            valid_line_found = True
            # This line is part of the diamond. Update bounding box.
            min_x = min(min_x, x1, x2)
            min_y = min(min_y, y1, y2)
            max_x = max(max_x, x1, x2)
            max_y = max(max_y, y1, y2)
    
    if not valid_line_found:
        return (0, 0)

    # Centroid
    centroid_x = int((min_x + max_x) / 2)
    centroid_y = int((min_y + max_y) / 2)

    return (centroid_x, centroid_y)


def template_match(img_orig, img_template, method):
    """Returns the location corresponding to match between original image and provided template.
    Args:
        img_orig (np.array) : numpy array representing 2-D image on which we need to find the template
        img_template: numpy array representing template image which needs to be matched within the original image
        method: corresponds to one of the four metrics used to measure similarity between template and image window
    Returns:
        Co-ordinates of the topmost and leftmost pixel in the result matrix with maximum match
    """
    """Each method is calls for a different metric to determine
       the degree to which the template matches the original image
       We are required to implement each technique using the
       sliding window approach.
       Suggestion : For loops in python are notoriously slow
       Can we find a vectorized solution to make it faster?
    """
    img_orig_f = img_orig.astype(float)
    img_template_f = img_template.astype(float)
    
    h_temp, w_temp = img_template_f.shape[:2]
    h_orig, w_orig = img_orig_f.shape[:2]

    result = np.zeros(
        (
            (h_orig - h_temp + 1),
            (w_orig - w_temp + 1),
        ),
        float,
    )
    
    top_left = (0, 0)
    """Once you have populated the result matrix with the similarity metric corresponding to each overlap, return the topmost and leftmost pixel of
    the matched window from the result matrix. You may look at Open CV and numpy post processing functions to extract location of maximum match"""
    if method == "tm_nssd" or method == "tm_nccor":
        eps = 1e-6 # Epsilon for numerical stability
        template_mean = np.mean(img_template_f)
        template_std = np.std(img_template_f) + eps
        template_norm = (img_template_f - template_mean) / template_std

    for y in range(result.shape[0]):
        for x in range(result.shape[1]):
            
            # Get the current window.
            window = img_orig_f[y : y + h_temp, x : x + w_temp]

            # Sum of squared differences.
            if method == "tm_ssd":
                result[y, x] = np.sum((window - img_template_f) ** 2)

            # Normalized sum of squared differences.
            elif method == "tm_nssd":
                window_mean = np.mean(window)
                window_std = np.std(window) + eps
                window_norm = (window - window_mean) / window_std
                
                result[y, x] = np.sum((window_norm - template_norm) ** 2)

            # Cross Correlation.
            elif method == "tm_ccor":
                result[y, x] = np.sum(window * img_template_f)

            # Normalized Cross Correlation.
            elif method == "tm_nccor":
                window_mean = np.mean(window)
                window_std = np.std(window) + eps
                window_norm = (window - window_mean) / window_std
                
                result[y, x] = np.sum(window_norm * template_norm)

            else:
                print("Invalid method specified!")
                return (0, 0)

    # SSD
    if method == "tm_ssd" or method == "tm_nssd":
        min_y, min_x = np.unravel_index(np.argmin(result), result.shape)
        top_left = (min_x, min_y) # (x, y) convention
        
    # CCOR
    elif method == "tm_ccor" or method == "tm_nccor":
        max_y, max_x = np.unravel_index(np.argmax(result), result.shape)
        top_left = (max_x, max_y) # (x, y) convention

    return top_left


'''Below is the helper code to print images for the report'''
#     cv2.rectangle(img_orig,top_left, bottom_right, 255, 2)
#     plt.subplot(121),plt.imshow(result,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img_orig,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(method)
#     plt.show()


def dft(x):
    """Discrete Fourier Transform for 1D signal
    Args:
        x (np.array): 1-dimensional numpy array of shape (n,) representing signal
    Returns:
        y (np.array): 1-dimensional numpy array of shape (n,) representing Fourier Transformed Signal

    """
    x = np.asarray(x, dtype=np.complex128)
    N = x.shape[0]
    
    k = np.arange(N)
    
    kx = np.outer(k, k)
    
    w = np.exp(-2j * np.pi / N)
    
    M = w ** kx
    
    y = M @ x
    
    return y



def idft(x):
    """Inverse Discrete Fourier Transform for 1D signal
    Args:
        x (np.array): 1-dimensional numpy array of shape (n,) representing Fourier-Transformed signal
    Returns:
        y (np.array): 1-dimensional numpy array of shape (n,) representing signal

    """
    x = np.asarray(x, dtype=np.complex128)
    N = x.shape[0]
    
    k = np.arange(N)
    
    kx = np.outer(k, k)
    
    w = np.exp(2j * np.pi / N)
    
    M = w ** kx
    
    y = (M @ x) / N
    
    return y


def dft2(img):
    """Discrete Fourier Transform for 2D signal
    Args:
        img (np.array): 2-dimensional numpy array of shape (n,m) representing image
    Returns:
        y (np.array): 2-dimensional numpy array of shape (n,m) representing Fourier-Transformed image

    """
    rows_dft = np.apply_along_axis(dft, 1, img)
    final_dft = np.apply_along_axis(dft, 0, rows_dft)
    
    return final_dft


def idft2(img):
    """Inverse Discrete Fourier Transform for 2D signal
    Args:
        img (np.array): 2-dimensional numpy array of shape (n,m) representing Fourier-Transformed image
    Returns:
        y (np.array): 2-dimensional numpy array of shape (n,m) representing image

    """
    rows_idft = np.apply_along_axis(idft, 1, img)
    final_idft = np.apply_along_axis(idft, 0, rows_idft)

    return final_idft


def compress_image_fft(img_bgr, threshold_percentage):
    """Return compressed image by converting to fourier domain, thresholding based on threshold percentage, and converting back to fourier domain
    Args:
        img_bgr (np.array): numpy array of shape (n,m,3) representing bgr image
        threshold_percentage (float): between 0 and 1 representing what percentage of Fourier image to keep
    Returns:
        img_compressed (np.array): numpy array of shape (n,m,3) representing compressed image. (Make sure the data type of the np array is float64)
        compressed_frequency_img (np.array): numpy array of shape (n,m,3) representing the compressed image in the frequency domain

    """
    img_compressed = np.zeros_like(img_bgr, dtype=np.float64)
    compressed_frequency_img = np.zeros_like(img_bgr, dtype=np.float64)
    
    for i in range(3):
        channel = img_bgr[:, :, i]
        
        F = np.fft.fft2(channel)
        
        mags = np.abs(F)
        sorted_mags = np.sort(mags.ravel())[::-1] # Sort descending.
        
        n_pixels = channel.size
        threshold_index = int(np.floor(threshold_percentage * n_pixels))
        
        if threshold_index >= len(sorted_mags):
            threshold_index = len(sorted_mags) - 1
            
        threshold_value = sorted_mags[threshold_index]
        
        mask = mags > threshold_value
        F_masked = F * mask
        
        channel_compressed = np.fft.ifft2(F_masked)
        
        # We must take the real part, as iFFT may have tiny imaginary components.
        img_compressed[:, :, i] = np.real(channel_compressed)
        
        # Shift, log-scale, and store.
        F_shifted_masked = np.fft.fftshift(F_masked)
        # Add epsilon (1e-9) to avoid log(0).
        freq_img_viz = 20 * np.log(np.abs(F_shifted_masked) + 1e-9)
        
        compressed_frequency_img[:, :, i] = freq_img_viz

    return img_compressed, compressed_frequency_img


def low_pass_filter(img_bgr, r):
    """Return low pass filtered image by keeping a circle of radius r centered on the frequency domain image
    Args:
        img_bgr (np.array): numpy array of shape (n,m,3) representing bgr image
        r (float): radius of low pass circle
    Returns:
        img_low_pass (np.array): numpy array of shape (n,m,3) representing low pass filtered image. (Make sure the data type of the np array is float64)
        low_pass_frequency_img (np.array): numpy array of shape (n,m,3) representing the low pass filtered image in the frequency domain

    """
    img_low_pass = np.zeros_like(img_bgr, dtype=np.float64)
    low_pass_frequency_img = np.zeros_like(img_bgr, dtype=np.float64)

    rows, cols, _ = img_bgr.shape
    cy, cx = rows // 2, cols // 2
    
    y, x = np.ogrid[:rows, :cols]
    
    dist_from_center = np.sqrt((x - cx)**2 + (y - cy)**2)
    
    mask = dist_from_center <= r
    
    for i in range(3):
        channel = img_bgr[:, :, i]
        
        F = np.fft.fft2(channel)
        
        F_shifted = np.fft.fftshift(F)

        F_shifted_masked = F_shifted * mask
        
        freq_img_viz = 20 * np.log(np.abs(F_shifted_masked) + 1e-9)
        low_pass_frequency_img[:, :, i] = freq_img_viz
        
        F_masked = np.fft.ifftshift(F_shifted_masked)
        
        channel_lpf = np.fft.ifft2(F_masked)
        
        img_low_pass[:, :, i] = np.real(channel_lpf)
        
    return img_low_pass, low_pass_frequency_img
