"""2-matrix-divided.py docstring test"""
def matrix_divided(matrix, div):
    """This function divided elements of a matrix by div
    args:
         matrix: list of list type int or float 
         div: type int or float no 0
    result:
         new matrix with divided results
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    row = len(matrix[0])
    new_matrix = list()

    for i in matrix:
        if len(i) != row:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = list()
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_list.append(round(j / div, 2))
        new_matrix.append(new_list)
    return new_matrix
