#!/usr/bin/python3


"""Square class from rectangle"""


from .base import Base
from .rectangle import Rectangle


class Square(Rectangle, Base):
    """class square that imports Rectangle and Base"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
