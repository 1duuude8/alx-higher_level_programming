#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns the key with highest value

    Args:
        a_dictionary (dict) : dict to be evaluated.It is assumed that
        all values are comparable (e.g., all numbers or all strings).


        return:
            key with highest value
    """
    if not a_dictionary:
        return None
    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key
