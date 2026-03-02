"""
Concatenate corresponding items of two lists of strings. 
- Input: list1 = ["Hello", "Good"] and list2 = ["World", "Morning"] 
- Output: ["Hello World", "Good Morning"]
"""

# Define the first list
list1 = ["Hello", "Good"]

# Define the second list
list2 = ["World", "Morning"]

result = list(map(lambda x, y: x + " " + y, list1, list2))

# Display the result
print(result)