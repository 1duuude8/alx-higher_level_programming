def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list on the same line followed by a new line.

    Parameters:
    my_list (list): The list from which elements will be printed.
    x (int): The number of elements to print from the list. Defaults to 0.

    Returns:
    int: The real number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")  # print element of the list at index 1
            count += 1  # increment counting if printing is succesful
        except IndexError:  # if anindex error occured
            break  # if index error occured break the loop
    print()
    return count
