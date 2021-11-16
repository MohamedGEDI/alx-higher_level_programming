#!/usr/bin/python3
"""import base class"""


from .base import Base
"""this is an rectangle class"""


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """import base constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """decorator getter property"""
        return self.__width

    @width.setter
    def width(self, width):
        """decorator setter property"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """decorator getter property"""
        return self.__height

    @height.setter
    def height(self, height):
        """decorator setter property"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """decorator getter property"""
        return self.__x

    @x.setter
    def x(self, x):
        """decorator setter property"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """decorator getter property"""
        return self.__y

    @y.setter
    def y(self, y):
        """decorator setter property"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def update(self, *args, **kwargs):
        """Update setting attributes"""
        i = 0
        attributes = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for attr in attributes:
                if i > len(args) - 1:
                    break
                setattr(self, attr, args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    continue
                setattr(self, key, value)

    def area(self):
        """area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """display the rectangle as # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def to_dictionary(self):
        """transform to dictionary"""
        rect = dict()
        rect = {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }
        return rect

    def __str__(self):
        """string representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
