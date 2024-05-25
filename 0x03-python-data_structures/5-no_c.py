#!/usr/bin/python3
def no_c(my_string):
    filter_c = [char for char in my_string if (char != "c" and char != "C")]
    new_string = "".join(filter_c)
    print(new_string)
