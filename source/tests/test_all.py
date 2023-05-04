# from source import *
# from augment import rotate, reflect, right_shift, upsample_scaling, augment_image
import augment
import unittest
import numpy as np

# from .. import augment
# from unittest.mock import patch

# UNIT TESTS


class TestMethods(unittest.TestCase):
    def test_is_matrix_square(self):
        non_square_matrix = [[1, 1, 1], [1, 1, 1]]
        assert augment.augment_image(non_square_matrix) == None

    def test_rotate(self):
        square_matrix = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        rotate_matrix = augment.rotate(square_matrix)
        assert rotate_matrix == [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

    def test_reflect(self):
        square_matrix = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        reflect_matrix = augment.reflect(square_matrix)
        assert reflect_matrix == [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

    def test_right_shift(self):
        square_matrix = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
        rs_matrix = augment.right_shift(square_matrix, 1)
        assert rs_matrix == [[0, 1, 1], [0, 1, 0], [0, 1, 0]]

    def test_upsample_scaling(self):
        square_matrix = [[1, 0], [0, 1]]
        us_matrix = augment.upsample_scaling(np.array(square_matrix)).tolist()
        assert us_matrix == [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]

    # INTEGRATION TEST
    def test_rotate_shift(self):
        square_matrix = [[0, 0, 0], [0, 0, 0], [1, 0, 1]]
        rotate_matrix = augment.rotate(square_matrix)
        rs_matrix = augment.right_shift(rotate_matrix, 1)
        final_matrix = augment.reflect(rs_matrix)
        assert final_matrix == [[0, 1, 0], [0, 0, 0], [0, 1, 0]]


# is_matrix_square()
# check_rotate()
# check_reflect()
# check_right_shift()
# check_upsample_scaling()
# check_rotate_shift()