#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == None:
        return None
    newlist = my_list.copy()
    l = len(my_list)
    for x in range(l):
        if newlist[x] == search:
            newlist[x] = replace
    return newlist
