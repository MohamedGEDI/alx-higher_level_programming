#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer
add_tuple = __import__('7-add_tuple').add_tuple
multiple_returns = __import__('8-multiple_returns').multiple_returns
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
tuple_a = (1, 89)
sentence = "trying again"
length, first = multiple_returns(sentence)
print("length {:d} - first letter {}".format(length, first))
