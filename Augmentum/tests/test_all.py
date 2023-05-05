# from source import *
# from augment import rotate, reflect, right_shift, upsample_scaling, augment_image
import main
import unittest
import numpy as np

# from .. import augment
# from unittest.mock import patch


class TestMethods(unittest.TestCase):
    # UNIT TESTS
    augmentum = main.Augmentum()

    def test_is_matrix_square(self):
        non_square_matrix = [[1, 1, 1], [1, 1, 1]]
        assert self.augmentum.augment_image(non_square_matrix) == None

    def test_rotate(self):
        square_matrix = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        rotate_matrix = self.augmentum.rotate(square_matrix)
        assert rotate_matrix == [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

    def test_reflect(self):
        square_matrix = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        reflect_matrix = self.augmentum.reflect(square_matrix)
        assert reflect_matrix == [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

    def test_right_shift(self):
        square_matrix = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
        rs_matrix = self.augmentum.right_shift(square_matrix, 1)
        assert rs_matrix == [[0, 1, 1], [0, 1, 0], [0, 1, 0]]

    def test_upsample_scaling(self):
        square_matrix = [[1, 0], [0, 1]]
        us_matrix = self.augmentum.upsample_scaling(np.array(square_matrix)).tolist()
        assert us_matrix == [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]

    # INTEGRATION TEST
    def test_rotate_shift(self):
        square_matrix = [[0, 0, 0], [0, 0, 0], [1, 0, 1]]
        rotate_matrix = self.augmentum.rotate(square_matrix)
        rs_matrix = self.augmentum.right_shift(rotate_matrix, 1)
        final_matrix = self.augmentum.reflect(rs_matrix)
        assert final_matrix == [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
