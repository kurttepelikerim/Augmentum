import numpy as np
from PIL import Image

#Given an n x n 2D matrix (list of lists) representing an image, rotates the image by 90 degrees (clockwise).
def rotate(matrix):
    size = len(matrix) 
    for i in range(size // 2 + size % 2):
        for j in range(size // 2):
            tmp = matrix[size-1-j][i]
            matrix[size-1-j][i] = matrix[size-1-i][size-1-j]
            matrix[size-1-i][size-1-j] = matrix[j][size-1-i]
            matrix[j][size-1-i] = matrix[i][j]
            matrix[i][j] = tmp
    return matrix

#Given an nxn 2D matrix (list of lists) reflect the image by its vertical central axis
def reflect(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
    return matrix

#shifts a numpy matrix to the right by x units
def shift_right(matrix, x):
    vect_shape = matrix.shape[:2]
    pp = np.full(shape=(vect_shape[0], x), fill_value=0)
    new_matrix = np.hstack(tup=(matrix, pp))
    return new_matrix

#scales the size of the image by a factor of 2
def scale(img, img_width, img_height):
    new_width = 2 * img_width
    new_height: int = 2 * img_height
    new_dim = (new_width, new_height)
    return img.resize(new_dim)

#given a binary image returns an image dataset (list of images) by appling image augmentation techniques
def augment(image):
    new_images = []

    img = Image.open(image)
    data = np.array(img)
    
    new_images.append(reflect(data.tolist()))
    new_images.append(rotate(data.tolist()))
    new_images.append(shift_right(data).tolist())
    new_images.append(np.array(scale(img, data.shape[0], data.shape[1])))

    return new_images
