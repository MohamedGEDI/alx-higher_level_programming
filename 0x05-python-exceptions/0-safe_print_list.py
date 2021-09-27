#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
    count = 0
    for i in my_list:
        count = count + 1
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return x
    except:
        print()
        return count
          
