"""
Check if all string in a list are palindromes.
"""

# List of the word
words = ["madam", "level", "radar"]

# Check if each word is equal to its reverse 
result = all(map(lambda x: x == x[::-1], words))

# Display the result
print(result)