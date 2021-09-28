#!/usr/bin/python3


"""simple square class"""


class Square:
    """initiated class"""
    def __init__(self, size=0):
        if (not isinstance(size, int)):
            raise TypeError("size must be integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        result = self.__size * self.__size
        return result
