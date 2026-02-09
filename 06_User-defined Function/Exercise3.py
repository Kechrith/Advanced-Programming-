""" Write a function called remove_items that will accept an item and a list, remove all the occurrences 
of the item from the list, then returns the lis
"""
def remove_items(item, lst):

    # create an empty list 
    new_list = []

    # check through each element in the original list
    for x in lst:

        # Check if the current element is not the item to be removed
        if x != item:
            new_list.append(x)
    # return the list after removing 
    return new_list

# Original List
numbers = [1, 2, 3, 2, 4, 2, 5]

# call the functiona and remove all occurences of 2
result = remove_items(2, numbers)

# Display the result
print(result)
