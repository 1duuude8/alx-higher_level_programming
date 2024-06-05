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
    new_list = list(map(lambda n: n * number, my_list))
    return new_list


my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)