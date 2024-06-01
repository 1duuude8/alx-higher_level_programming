#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    calculate the sum of unique element of a list

    args :
        my_list (list) : list of integer

    return :
        int : the sum of unique element in a list
    """
    return sum(set(my_list))
