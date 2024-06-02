#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary sorted by keys in ascending order.

    Args:
        a_dictionary(dict): The dict to be sorted and printed.
    Return:
        None
    """
    sorted_list = sorted(a_dictionary.items())
    for i, v in sorted_list:  # iterates over sorted dict
        print("{}: {}".format(i, v))  # print each key-value pair
