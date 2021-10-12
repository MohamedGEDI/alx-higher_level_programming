#!/usr/bin/python3
"""import all files and modules"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


alist = list()
for arg in sys.argv[1:]:
    alist.append(arg)

try:
    data = load_from_json_file("add_item.json")
except Exception:
    data = []

data.extend(alist)
save_to_json_file(data, "add_item.json")
