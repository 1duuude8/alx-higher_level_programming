#!/usr/bin/python3
def multiple_returns(sentence):
    """
    return a tuple with value of lenght and first char
    id sentence is empty , first chat is empty
    Args :
    sentence the input string

    returns:
    tuple with lenght of str and first char of str
    """
    lenght = len(sentence)
    first = sentence[0] if sentence else None
    return lenght, first
