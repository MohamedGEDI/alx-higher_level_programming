#!/usr/bin/python3


"""simple square class"""


class Square:
    """initiated class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        result = self.__size * self.__size
        return result

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
