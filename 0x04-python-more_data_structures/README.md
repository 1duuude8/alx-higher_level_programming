 here are tasks description :
Tasks :
task 0. Squared simple


Write a function that computes the square value of all integers of a matrix.

    Prototype: def square_matrix_simple(matrix=[]):
    matrix is a 2 dimensional array
    Returns a new matrix:
        Same size as matrix
        Each value should be the square of the value of the input
    Initial matrix should not be modified
    You are not allowed to import any module
    You are allowed to use regular loops, map, etc.

guillaume@ubuntu:~/0x04$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 


task 1. Search and replace
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that replaces all occurrences of an element by another in a new list.

    Prototype: def search_replace(my_list, search, replace):
    my_list is the initial list
    search is the element to replace in the list
    replace is the new element
    You are not allowed to import any module

guillaume@ubuntu:~/0x04$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/0x04$

Task 2 :Unique addition

Write a function that adds all unique integers in a list (only once for each integer).

    Prototype: def uniq_add(my_list=[]):
    You are not allowed to import any module

guillaume@ubuntu:~/0x04$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
guillaume@ubuntu:~/0x04$ 


task 3 : Present in both

Write a function that returns a set of common elements in two sets.

    Prototype: def common_elements(set_1, set_2):
    You are not allowed to import any module

guillaume@ubuntu:~/0x04$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/0x04$ ./3-main.py
['C']
guillaume@ubuntu:~/0x04$ 

Task 4: Only differents

Write a function that returns a set of all elements present in only one set.

    Prototype: def only_diff_elements(set_1, set_2):
    You are not allowed to import any module

guillaume@ubuntu:~/0x04$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/0x04$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/0x04$ 


Task 5: Number of keys

Write a function that returns the number of keys in a dictionary.

    Prototype: def number_keys(a_dictionary):
    You are not allowed to import any module

guillaume@ubuntu:~/0x04$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$ 


Task 6: Print sorted dictionary

Write a function that prints a dictionary by ordered keys.

    Prototype: def print_sorted_dictionary(a_dictionary):
    You can assume that all keys are strings
    Keys should be sorted by alphabetic order
    Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
    Dictionary values can have any type
    You are not allowed to import any module

guillaume@ubuntu:~/0x04$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/0x04$ 

Task 7:
. Update dictionary
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that replaces or adds key/value in a dictionary.

    Prototype: def update_dictionary(a_dictionary, key, value):
    key argument will be always a string
    value argument will be any type
    If a key exists in the dictionary, the value will be replaced
    If a key doesn’t exist in the dictionary, it will be created
    You are not allowed to import any module

guillaume@ubuntu:~/0x04$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/0x04$ 


Task 9: Multiply by 2
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that returns a new dictionary with all values multiplied by 2

    Prototype: def multiply_by_2(a_dictionary):
    You can assume that all values are only integers
    Returns a new dictionary
    You are not allowed to import any module



Task 10:S

Write a function that returns a key with the biggest integer value.

    Prototype: def best_score(a_dictionary):
    You can assume that all values are only integers
    If no score found, return None
    You can assume all students have a different score
    You are not allowed to import any module

guillaume@ubuntu:~/0x04$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

guillaume@ubuntu:~/0x04$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/0x04$ 


Task 11. Multiply by using map

Write a function that returns a list with all values multiplied by a number without using any loops.

    Prototype: def multiply_list_map(my_list=[], number=0):
    Returns a new list:
        Same length as my_list
        Each value should be multiplied by number
    Initial list should not be modified
    You are not allowed to import any module
    You have to use map
    Your file should be max 3 lines

guillaume@ubuntu:~/0x04$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/0x04$ 










