#!/usr/bin/python3
"""inherit base geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """functions on rectangle"""
    def __init__(self, width, height):
        """validate and initiate class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
