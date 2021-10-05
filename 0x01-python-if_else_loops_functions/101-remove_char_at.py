#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        str[n] = ''
    print("{}".format(str), end='')


remove_char_at("holberton", 3)
