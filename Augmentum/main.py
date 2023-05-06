import numpy as np


class Augmentum:
    def rotate(self, matrix):
        """
        Given a binary image (list of lists) rotates it by 90 degrees (clockwise).

        :param matrix: matrix representing the grayscale image
        :type kind: list of lists
        :return: grayscale image rotated by 90 degreees (clockwise)
        :rtype: list of lists
        """
        size = len(matrix)
        for i in range(size // 2 + size % 2):
            for j in range(size // 2):
                tmp = matrix[size - 1 - j][i]
                matrix[size - 1 - j][i] = matrix[size - 1 - i][size - 1 - j]
                matrix[size - 1 - i][size - 1 - j] = matrix[j][size - 1 - i]
                matrix[j][size - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
        return matrix

    def reflect(self, matrix):
        """
        Given a binar image (list of lists) reflects it by its vertical central axis

        :param matrix: matrix representing the grayscale image
        :type kind: list of lists
        :return: grayscale image reflected by its vertical central axis
        :rtype: list of lists
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
        return matrix

    def right_shift(self, matrix, x):
        """
        Given a binary image (list of lists) shifts it to the right
        by x units (fills left values with 0)

        :param matrix: matrix representing the grayscale image
        :type kind: list of lists
        :param x: unit for right shift
        :type kind: integer
        :return: grayscale image shifted right by x units
        :rtype: list of lists
        """
        new_matrix = [[] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(x):
                new_matrix[i].append(0)
            for j in range(len(matrix[0]) - x):
                new_matrix[i].append(matrix[i][j])
        return new_matrix

    def upsample_scaling(self, matrix):
        """
        Given a binary image (list of lists) scales the size of it by a factor of 2 by upsampling

        :param matrix: matrix representing the grayscale image
        :type kind: list of lists
        :return: grayscale image scaled by a factor of 2
        :rtype: list of lists
        """
        # smaller_img = bigger_img[::2, ::2]
        bigger_img = matrix.repeat(2, axis=0).repeat(2, axis=1)
        return bigger_img

    def augment_image(self, image_matrix):
        """
        Given a binary image (list of lists) returns an image dataset (list of images)
        by appling image augmentation techniques

        :param matrix: matrix representing the grayscale image
        :type kind: list of lists
        :return: image dataset
        :rtype: list of lists of lists
        """
        if len(image_matrix) != len(image_matrix[0]):
            return None
        new_images = []
        new_images.append(self.rotate(image_matrix))
        new_images.append(self.reflect(image_matrix))
        new_images.append(self.right_shift(image_matrix, 5))
        new_images.append(self.upsample_scaling(np.array(image_matrix)))
        return new_images
