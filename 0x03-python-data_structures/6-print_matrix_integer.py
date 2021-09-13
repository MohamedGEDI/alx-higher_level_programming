#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            if j == c-1:
                print("{}".format(matrix[i][j]), end='')
                continue
            print("{} ".format(matrix[i][j]), end='')
        print("")
