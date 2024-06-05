#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    return new lis with all its element*number

    Args:
        my_list (list) : contains element to be evaluated
        number (int) : number we use to multply list elements

    return
        list: A new list containing the multiplied elements
    """
    return list(map(lambda x: x * number, my_list))
