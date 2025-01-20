#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
print("Original list:", my_list)
new_list = replace_in_list(my_list, idx, new_element)
print("New list:", new_list)

# Testing invalid index
idx = 5
new_list = replace_in_list(my_list, idx, new_element)
print("List after invalid index:", new_list)

# Testing negative index
idx = -1
new_list = replace_in_list(my_list, idx, new_element)
print("List after negative index:", new_list)
