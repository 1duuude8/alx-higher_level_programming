#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    change the vlue of key if its exist,
    if not it creat new one

    Args:
    a_dictionary(dict): dic to be modified
    key (str): The key whose value needs to be updated or added.
    value: The value to be assigned to the key.

    return:
        returns  dict with updated value
    """
    a_dictionary[key] = value
    return a_dictionary
