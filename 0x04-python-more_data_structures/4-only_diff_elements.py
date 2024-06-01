#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Return a set of elements that are in either of the sets but not in both.

    args:
        set_1 (set): the first set
        set_2 (set): the second set

    returns:
        set: containing elements that are in either of sets but not in both.
    """
    return set_1 ^ set_2
