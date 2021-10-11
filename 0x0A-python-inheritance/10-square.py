#!/usr/bin/python3
"""import necessary classes"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square """
    def __init__(self, size):
        """initialize square"""
        super().integer_validator("size", size)
        self.__size = size

    def area():
        return self.__size ** 2
