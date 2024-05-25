task 0:

0. Print a list of integers
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that prints all integers of a list.

    Prototype: def print_list_integer(my_list=[]):
    Format: one integer per line. See example
    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x03-python-data_structures
    File: 0-print_list_integer.py
task 1:

1. Secure access to an element in a list
mandatory
Score: 50.0% (Checks completed: 100.0%)

Write a function that retrieves an element from a list like in C.

    Prototype: def element_at(my_list, idx):
    If idx is negative, the function should return None
    If idx is out of range (> of number of element in my_list), the function should return None
    You are not allowed to import any module
    You are not allowed to use try/except
task 2 :

2. Replace element
mandatory
Score: 50.0% (Checks completed: 100.0%)

Write a function that replaces an element of a list at a specific position (like in C).

    Prototype: def replace_in_list(my_list, idx, element):
    If idx is negative, the function should not modify anything, and returns the original list
    If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
    You are not allowed to import any module
    You are not allowed to use try/except
task 3 :

3. Print a list of integers... in reverse!
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that prints all integers of a list, in reverse order.

    Prototype: def print_reversed_list_integer(my_list=[]):
    Format: one integer per line. See example
    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers
Task 4 :
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

    Prototype: def new_in_list(my_list, idx, element):
    If idx is negative, the function should return a copy of the original list
    If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
    You are not allowed to import any module
    You are not allowed to use try/except

guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 