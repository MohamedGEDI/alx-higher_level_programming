#!/usr/bin/python3
import sys

alist = [1, "yes", True, 3.14]

for arg in sys.argv[1:]:
    alist.append(arg)

print(alist)
