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

Task 5 :

5. Can you C me now?
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that removes all characters c and C from a string.

    Prototype: def no_c(my_string):
    The function should return the new string
    You are not allowed to import any module
    You are not allowed to use str.replace()

guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
Task 7 :

7. Tuples addition
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that adds 2 tuples.

    Prototype: def add_tuple(tuple_a=(), tuple_b=()):
    Returns a tuple with 2 integers:
        The first element should be the addition of the first element of each argument
        The second element should be the addition of the second element of each argument
    You are not allowed to import any module
    You can assume that the two tuples will only contain integers
    If a tuple is smaller than 2, use the value 0 for each missing integer
    If a tuple is bigger than 2, use only the first 2 integers
Task 8 :

8. More returns!
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that returns a tuple with the length of a string and its first character.

    Prototype: def multiple_returns(sentence):
    If the sentence is empty, the first character should be equal to None
    You are not allowed to import any module

task 9 :
Write a function that finds the biggest integer of a list.

    Prototype: def max_integer(my_list=[]):
    If the list is empty, return None
    You can assume that the list only contains integers
    You are not allowed to import any module
    You are not allowed to use the builtin max()

guillaume@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$ 

Task 10 :
0. Only by 2
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that finds all multiples of 2 in a list.

    Prototype: def divisible_by_2(my_list=[]):
    Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
    The new list should have the same size as the original list
    You are not allowed to import any module

guillaume@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$ 

task 11:

11. Delete at
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that deletes the item at a specific position in a list.

    Prototype: def delete_at(my_list=[], idx=0):
    If idx is negative or out of range, nothing change (returns the same list)
    You are not allowed to use pop()
    You are not allowed to import any module

guillaume@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$ 
