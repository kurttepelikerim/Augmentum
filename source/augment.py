import numpy as np


# Given an n x n 2D matrix (list of lists) representing an image, rotates the image by 90 degrees (clockwise).
def rotate(matrix):
    size = len(matrix)
    for i in range(size // 2 + size % 2):
        for j in range(size // 2):
            tmp = matrix[size - 1 - j][i]
            matrix[size - 1 - j][i] = matrix[size - 1 - i][size - 1 - j]
            matrix[size - 1 - i][size - 1 - j] = matrix[j][size - 1 - i]
            matrix[j][size - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp
    return matrix


# Given an nxn 2D matrix (list of lists) reflect the image by its vertical central axis
def reflect(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
    return matrix


# Given an nxn 2D matrix shifts the matrix to the right by x units (fills left values with 0)
def right_shift(matrix, x):
    new_matrix = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(x):
            new_matrix[i].append(0)
        for j in range(len(matrix[0]) - x):
            new_matrix[i].append(matrix[i][j])
    return new_matrix


# Scales the size of the image by a factor of 2 by upsampling
def upsample_scaling(matrix):
    # smaller_img = bigger_img[::2, ::2]
    bigger_img = matrix.repeat(2, axis=0).repeat(2, axis=1)
    return bigger_img


# Given a binary image(list of lists) returns an image dataset (list of images) by appling image augmentation techniques
def augment_image(image_matrix):
    if len(image_matrix) != len(image_matrix[0]):
        return None
    new_images = []
    new_images.append(rotate(image_matrix))
    new_images.append(reflect(image_matrix))
    new_images.append(right_shift(image_matrix, 5))
    new_images.append(upsample_scaling(np.array(image_matrix)))
    return new_images
