# Exercise5: Calculate the sum of each row 2D list 

# Create a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Use a lambda function to calculate the sum of each row    
row_sums = list(map(lambda row: sum(row), matrix))

# Print the result
print("The sum of each row is: ", row_sums)