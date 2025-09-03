import math
import numpy as np
import cv2

# # Implement the functions below.


def extract_red(image):
    """ Returns the red channel of the input image. It is highly recommended to make a copy of the
    input image in order to avoid modifying the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 2D array containing the red channel.
    """

    return image[:, :, 2].copy()


def extract_green(image):
    """ Returns the green channel of the input image. It is highly recommended to make a copy of the
    input image in order to avoid modifying the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 2D array containing the green channel.
    """
    
    return image[:, :, 1].copy()


def extract_blue(image):
    """ Returns the blue channel of the input image. It is highly recommended to make a copy of the
    input image in order to avoid modifying the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 2D array containing the blue channel.
    """
    
    return image[:, :, 0].copy()


def swap_green_blue(image):
    """ Returns an image with the green and blue channels of the input image swapped. It is highly
    recommended to make a copy of the input image in order to avoid modifying the original array.
    You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 3D array with the green and blue channels swapped.
    """
    
    temp_img = image.copy()
    temp_img[:, :, [0, 1]] = temp_img[:, :, [1, 0]]
    return temp_img


def copy_paste_middle(src, dst, shape):
    """ Copies the middle region of size shape from src to the middle of dst. It is
    highly recommended to make a copy of the input image in order to avoid modifying the
    original array. You can do this by calling:
    temp_image = np.copy(image)

        Note: Assumes that src and dst are monochrome images, i.e. 2d arrays.

        Note: Where 'middle' is ambiguous because of any difference in the oddness
        or evenness of the size of the copied region and the image size, the function
        rounds downwards.  E.g. in copying a shape = (1,1) from a src image of size (2,2)
        into an dst image of size (3,3), the function copies the range [0:1,0:1] of
        the src into the range [1:2,1:2] of the dst.

    Args:
        src (numpy.array): 2D array where the rectangular shape will be copied from.
        dst (numpy.array): 2D array where the rectangular shape will be copied to.
        shape (tuple): Tuple containing the height (int) and width (int) of the section to be
                       copied.

    Returns:
        numpy.array: Output monochrome image (2D array)
    """

    result = np.copy(dst)
    
    copy_height, copy_width = shape
    
    src_center_y = src.shape[0] // 2
    src_center_x = src.shape[1] // 2
    
    dst_center_y = dst.shape[0] // 2
    dst_center_x = dst.shape[1] // 2
    
    src_start_y = src_center_y - copy_height // 2
    src_end_y = src_start_y + copy_height
    src_start_x = src_center_x - copy_width // 2
    src_end_x = src_start_x + copy_width
    
    dst_start_y = dst_center_y - copy_height // 2
    dst_end_y = dst_start_y + copy_height
    dst_start_x = dst_center_x - copy_width // 2
    dst_end_x = dst_start_x + copy_width
    
    result[dst_start_y:dst_end_y, dst_start_x:dst_end_x] = src[src_start_y:src_end_y, src_start_x:src_end_x]
    
    return result



def copy_paste_middle_circle(src, dst, radius):
    """ Copies the middle circle region of radius "radius" from src to the middle of dst. It is
    highly recommended to make a copy of the input image in order to avoid modifying the
    original array. You can do this by calling:
    temp_image = np.copy(image)

        Note: Assumes that src and dst are monochrome images, i.e. 2d arrays.

    Args:
        src (numpy.array): 2D array where the circular shape will be copied from.
        dst (numpy.array): 2D array where the circular shape will be copied to.
        radius (scalar): scalar value of the radius.

    Returns:
        numpy.array: Output monochrome image (2D array)
    """

    result = np.copy(dst)
    
    src_y, src_x = np.ogrid[:src.shape[0], :src.shape[1]]
    dst_y, dst_x = np.ogrid[:dst.shape[0], :dst.shape[1]]
    
    src_r, src_c = (src.shape[0] - 1) // 2, (src.shape[1] - 1) // 2
    src_mask = (src_x - src_c) ** 2 + (src_y - src_r) ** 2 <= radius ** 2
    
    dst_r, dst_c = (dst.shape[0] - 1) // 2, (dst.shape[1] - 1) // 2
    dst_mask = (dst_x - dst_c) ** 2 + (dst_y - dst_r) ** 2 <= radius ** 2
    
    for i in range(dst.shape[0]):
        for j in range(dst.shape[1]):
            if dst_mask[i, j]:
                src_i = i - dst_r + src_r
                src_j = j - dst_c + src_c
                
                if (0 <= src_i < src.shape[0] and 
                    0 <= src_j < src.shape[1] and 
                    src_mask[src_i, src_j]):
                    result[i, j] = src[src_i, src_j]
    
    return result


def image_stats(image):
    """ Returns the tuple (min,max,mean,stddev) of statistics for the input monochrome image.
    In order to become more familiar with Numpy, you should look for pre-defined functions
    that do these operations i.e. numpy.min.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input 2D image.

    Returns:
        tuple: Four-element tuple containing:
               min (float): Input array minimum value.
               max (float): Input array maximum value.
               mean (float): Input array mean / average value.
               stddev (float): Input array standard deviation.
    """
    
    # First changing to float
    image = image.astype(float)
    return np.min(image), np.max(image), np.mean(image), np.std(image)


def center_and_normalize(image, scale):
    """ Returns an image with the same mean as the original but with values scaled about the
    mean so as to have a standard deviation of "scale".

    Note: This function makes no defense against the creation
    of out-of-range pixel values.  Consider converting the input image to
    a float64 type before passing in an image.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input 2D image.
        scale (int or float): scale factor.

    Returns:
        numpy.array: Output 2D image.
    """
    
    image = image.astype(np.float64)
    mean = np.mean(image)
    
    image = image - mean
    image = image * scale / np.std(image)
    image = image + mean
    
    return image



def shift_image_left(image, shift):
    """ Outputs the input monochrome image shifted shift pixels to the left.

    The returned image has the same shape as the original with
    the BORDER_REPLICATE rule to fill-in missing values.  See

    http://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/copyMakeBorder/copyMakeBorder.html?highlight=copy

    for further explanation.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input 2D image.
        shift (int): Displacement value representing the number of pixels to shift the input image.
            This parameter may be 0 representing zero displacement.

    Returns:
        numpy.array: Output shifted 2D image.
    """

    result = np.copy(image)
    
    if shift > 0:
        result[:, :-shift] = image[:, shift:]
        result[:, -shift:] = image[:, -1:]
    elif shift < 0:
        shift = abs(shift)
        result[:, shift:] = image[:, :-shift]
        result[:, :shift] = image[:, :1]
    
    return result

def difference_image(img1, img2):
    """ Returns the difference between the two input images (img1 - img2). The resulting array must be normalized
    and scaled to fit [0, 255].

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        img1 (numpy.array): Input 2D image.
        img2 (numpy.array): Input 2D image.

    Returns:
        numpy.array: Output 2D image containing the result of subtracting img2 from img1.
    """

    img1_copy = np.copy(img1).astype(np.float64)
    img2_copy = np.copy(img2).astype(np.float64)

    diff = img1_copy - img2_copy
    
    min_val = np.min(diff)
    max_val = np.max(diff)
    
    if max_val == min_val:
        return np.zeros_like(diff, dtype=np.float64)
    
    diff_normalized = (diff - min_val) / (max_val - min_val)
    
    diff_scaled = diff_normalized * 255.0
    
    return diff_scaled


def add_noise(image, channel, sigma):
    """ Returns a copy of the input color image with Gaussian noise added to
    channel (0-2). The Gaussian noise mean must be zero. The parameter sigma
    controls the standard deviation of the noise.

    The returned array values must not be clipped or normalized and scaled. This means that
    there could be values that are not in [0, 255].

    Note: This function makes no defense against the creation
    of out-of-range pixel values.  Consider converting the input image to
    a float64 type before passing in an image.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): input RGB (BGR in OpenCV) image.
        channel (int): Channel index value.
        sigma (float): Gaussian noise standard deviation.

    Returns:
        numpy.array: Output 3D array containing the result of adding Gaussian noise to the
            specified channel.
    """

    result = np.copy(image).astype(np.float64)
    
    noise = np.random.normal(0, sigma, image.shape)
    
    result[:, :, channel] += noise[:, :, channel]
    
    return result


def build_hybrid_image(image1, image2, cutoff_frequency):
    """ 
    Takes two images and creates a hybrid image given a cutoff frequency.
    Args:
        image1: numpy nd-array of dim (m, n, c)
        image2: numpy nd-array of dim (m, n, c)
        cutoff_frequency: scalar
    
    Returns:
        hybrid_image: numpy nd-array of dim (m, n, c)

    Credits:
        Assignment developed based on a similar project by James Hays. 
    """

    filter = cv2.getGaussianKernel(ksize=cutoff_frequency*4+1,
                                   sigma=cutoff_frequency)
    filter = np.dot(filter, filter.T)
    
    low_frequencies = cv2.filter2D(image1,-1,filter)

    high_frequencies = image2 - cv2.filter2D(image2,-1,filter)
    
    hybrid_image = low_frequencies + high_frequencies
    
    return hybrid_image


def vis_hybrid_image(hybrid_image):
    """ 
    Tools to visualize the hybrid image at different scale.

    Credits:
        Assignment developed based on a similar project by James Hays. 
    """


    scales = 5
    scale_factor = 0.5
    padding = 5
    original_height = hybrid_image.shape[0]
    num_colors = 1 if hybrid_image.ndim == 2 else 3

    output = np.copy(hybrid_image)
    cur_image = np.copy(hybrid_image)
    for scale in range(2, scales+1):
      # add padding
      output = np.hstack((output, np.ones((original_height, padding, num_colors),
                                          dtype=np.float32)))

      # downsample image
      cur_image = cv2.resize(cur_image, (0, 0), fx=scale_factor, fy=scale_factor)

      # pad the top to append to the output
      pad = np.ones((original_height-cur_image.shape[0], cur_image.shape[1],
                     num_colors), dtype=np.float32)
      tmp = np.vstack((pad, cur_image))
      output = np.hstack((output, tmp))

    return output
