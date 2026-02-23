'''
Exercise6:
Compare corresponding items of two lists and return "list1" if the item from the list1 is larger, 
otherwise return "list2". 
'''

# Define the two lists
list1 = [3, 8, 15]
list2 = [5, 7, 10]

# Use a list comprehension to compare corresponding items of the two lists
result = [
    "list1" if item1 > item2 else "list2"
    for item1, item2 in zip(list1, list2)
]
# print the result
print(result)