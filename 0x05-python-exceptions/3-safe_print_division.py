#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        return result
    except:
        result = "None"
        return result
    finally:
        print("Inside finally: {}".format(result))
