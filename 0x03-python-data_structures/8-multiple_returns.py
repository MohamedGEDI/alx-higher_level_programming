#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        first_letter = None
    else:
        first_letter = sentence[0]
    tuple_r = (l, first_letter)
    return tuple_r
