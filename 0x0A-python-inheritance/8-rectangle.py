#!/ust/bin/python3
"""inherit base geometry"""


class Rectangle(BaseGeometry):
    """functions on rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
