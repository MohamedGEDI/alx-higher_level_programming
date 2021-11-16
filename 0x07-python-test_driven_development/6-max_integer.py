"""find max in a list"""
def max_integer(list=[]):
    """Get max of a list
       args:
            list - of type(list)
       Return:
            largest number
    """
    if len(list) == 0:
        return None
    return max(list)
