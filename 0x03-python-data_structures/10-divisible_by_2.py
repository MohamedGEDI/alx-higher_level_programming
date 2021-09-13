#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l = len(my_list)
    list_result = []
    for i in range(l):
        if my_list[i] % 2 == 0:
            list_result.append(True)
        elif my_list[i] % 2 != 0:
            list_result.append(False)
    return list_result
