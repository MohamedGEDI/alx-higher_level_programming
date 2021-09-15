#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == None:
        return None
    else:
        new_matrix = [[n * n for n in a] for a in matrix]
        return new_matrix
