from source import *

#UNIT TESTS

def is_matrix_square():
    non_square_matrix = [[1,1,1],[1,1,1]]
    assert(augment(non_square_matrix) == None)

def check_rotate():
    square_matrix = [[1,1,1],[0,0,0],[0,0,0]]
    rotate_matrix = rotate(square_matrix)
    assert(rotate_matrix == [[0, 0, 1], [0, 0, 1], [0, 0, 1]])

def check_reflect():
    square_matrix = [[1,0,0],[1,0,0],[1,0,0]]
    reflect_matrix = reflect(square_matrix)
    assert(reflect_matrix == [[0, 0, 1], [0, 0, 1], [0, 0, 1]])

def check_right_shift():
    square_matrix = [[1,1,1],[1,0,0],[1,0,0]]
    rs_matrix = right_shift(square_matrix,1)
    assert(rs_matrix == [[0, 1, 1], [0, 1, 0], [0, 1, 0]])

def check_upsample_scaling():
    square_matrix = [[1,0],[0,1]]
    us_matrix = upsample_scaling(np.array(square_matrix)).tolist()
    assert(us_matrix == [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])

#INTEGRATION TEST

def check_rotate_shift():
    square_matrix = [[0,0,0],[0,0,0],[1,0,1]]
    rotate_matrix = rotate(square_matrix)
    rs_matrix = right_shift(rotate_matrix,1)
    final_matrix = reflect(rs_matrix)
    assert(final_matrix == [[0, 1, 0], [0, 0, 0], [0, 1, 0]])

#is_matrix_square()
#check_rotate()
#check_reflect()
#check_right_shift()
#check_upsample_scaling()
#check_rotate_shift()
