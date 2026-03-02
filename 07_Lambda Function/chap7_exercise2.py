"""
Calculate (2x)^2 for each number in a list
"""

numbers = [1, 2, 3, 4]

# Apply lambda to compute (2x)^2
result2 = list(map(lambda x: (2 * x) ** 2, numbers))

print("Result:", result2)