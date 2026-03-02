"""
Filter numbers that are divisible by 3 and not divisible by 2 from a list
"""

# Create a list of numbers
numbers = [1, 3, 6, 9, 12, 15, 18]

# filter numbers divisible by 3 and not divisible by 2
result = list(filter(lambda x: x % 3 == 0 and x % 2 != 0, numbers))

# Display result
print(result)