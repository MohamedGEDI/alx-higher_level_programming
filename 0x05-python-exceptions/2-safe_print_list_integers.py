#!/usr/bin/python3
def safe_print_list_int(mylist=[], x=0):
    test = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            test = test + 1
        except ValueError:
            pass
        except TypeError:
            pass
    print("")
    return test
          
