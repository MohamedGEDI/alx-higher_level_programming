#!/usr/bin/python3
"""Class rectangle inherits from base class"""
from models.base import Base

class Rectangle(Base):
    """Put super of base class init"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ inherit super """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
 
     
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            if type(width) is not int:
                raise TypeError("Must be an int")
            else:
                self.__width = width
        
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            if type(height) is not int:
                raise TypeError("Must be an int")
            else:
                self.__height = height

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, x):
            if type(x) is not int:
                raise TypeError("Must be an int")
            else:
                self.__x = x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, y):
            if type(y) is not int:
                raise TypeError("Must be an int")
            else:
                self.__y = y
