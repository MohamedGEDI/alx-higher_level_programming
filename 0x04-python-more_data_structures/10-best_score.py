#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        temp = -99
        for k, v in a_dictionary.items():
            if temp <= v:
                temp = v
        key_list = list(a_dictionary.keys())
        val_list = list(a_dictionary.values())
        position = val_list.index(temp)
        return key_list[position]
