def search_replace(my_list, search, replace):
    """
    replaces all occurrences of 'search' by 'replace' in a new list
    if it exist
    args:
        my_list(list) : the initial lits
        search : targeted element to replace
        replace : the new element to replace 'search'
    return:
        new list with replaced element
    """
    return [replace if element == search else element for element in my_list]
