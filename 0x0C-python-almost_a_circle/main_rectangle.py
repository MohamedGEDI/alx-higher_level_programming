#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":
    ri = Rectangle(10, 2)
    print(ri.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
