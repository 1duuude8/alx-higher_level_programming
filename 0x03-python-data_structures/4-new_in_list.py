#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        shallow_list = my_list.copy()
    elif idx >= len(my_list):
        shallow_list = my_list.copy()
    else:
        shallow_list = my_list.copy()
        shallow_list[idx] = element
    return shallow_list
