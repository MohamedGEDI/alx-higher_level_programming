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
                raise TypeError("width must be an int")
            elif width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width
        
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            if type(height) is not int:
                raise TypeError("height must be an int")
            elif height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, x):
            if type(x) is not int:
                raise TypeError("x must be an int")
            elif x < 0:
                raise ValueError("x must be > 0")
            else:
                self.__x = x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, y):
            if type(y) is not int:
                raise TypeError("y be an int")
            elif y < 0:
                raise ValueError("y must be > 0")
            else:
                self.__y = y

        def update(self, *args, **kwargs):
            i = 0
            attributes = ['id', 'width', 'height', 'x', 'y']
            if len(args) > 0:
                for attr in attributes:
                    if i > len(args) - 1:
                        break
                    setattr(self, attr, args[i])
            else:
                for key, value in kwargs.items():
                    if key not in attributes:
                        continue
                    setattr(self, key, value)
                        

        def area(self):
            return self.__width * self.__height

        def display(self):
            for i in range(self.__y):
                print()
            for i in range(self.__height):
                print(" " * self.__x  + "#" * self.__width)

        def __str__(self):
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
