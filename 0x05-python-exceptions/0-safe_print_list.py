#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
    test = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            test = test + 1
        except IndexError:
            break
    print('')
    return test
