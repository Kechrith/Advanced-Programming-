"""
Convert all strings in the list to lowercase
"""

# Use map() with lambda to apply .lower() to each string
strings = ["Hello", "WORLD", "PyThOn"]

result3 = list(map(lambda s: s.lower(), strings))

print("Lowercase:", result3)