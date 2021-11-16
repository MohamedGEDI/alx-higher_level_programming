#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    if a == 2 and b == 2:
        add_0 = tuple_a[0] + tuple_b[0]
        add_1 = tuple_a[1] + tuple_b[1]
        add = (add_0, add_1)
    elif a < 2 or b < 2:
        if a == 0 or b == 0:
             tuple_a = 0, 0
             tuple_b = 0, 0
        elif a == 1 or b == 1:
             tuple_a = tuple_a[0], 0
             tuple_b = tuple_b[0], 0
        add_0 = tuple_a[0] + tuple_b[0]
        add_1 = tuple_a[1] + tuple_b[1]
        add = (add_0, add_1) 
    return add
