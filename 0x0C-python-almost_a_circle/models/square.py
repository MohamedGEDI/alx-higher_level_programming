#!/usr/bin/python3


"""Square class from rectangle"""


from .base import Base
from .rectangle import Rectangle


"""import other classes"""


class Square(Rectangle, Base):
    """class square that imports Rectangle and Base"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor imported from Rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
