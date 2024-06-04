#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    delete a pair of key if it exist

    Args:
        a_dictionari (dict) to be modified
        key (str): they key to be deleted

    returns :
        updated dict
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
