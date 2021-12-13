#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":
<<<<<<< HEAD

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

=======
    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)
>>>>>>> bca4019cebaba6c8d00aa1918de7ac51e1747eb0
