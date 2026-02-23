"""
Check if any number in a list is divisible by both 3 and 5. 
"""
# list of the number
numbers = [2, 4, 10, 15, 20]

# Check if any number is divisible by 3 and 5
result = any(map(lambda x: x % 15 == 0, numbers))

# Dislay result
print(result)