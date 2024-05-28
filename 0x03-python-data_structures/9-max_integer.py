#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]
    for items in my_list[1:0]:
        if items > max_value:
            max_value = items
    return max_value
