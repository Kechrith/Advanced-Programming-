'''
Exercise 2
Write  a  program  that creates  a  list  with  5  elements  and  asks  the  user to input  an  index.  Display  the 
element at that index. Handle: 
- IndexError if the index is out of bounds 
- ValueError if the entered value is not integer.
'''

# Create a list with 5 elements
my_list = [10, 20, 30, 40, 50]

try:
    # Ask the user to enter an index
    index = int(input("Enter an index : "))
    print("The element at index", index, "is:", my_list[index])
    
# Handle the IndexError case where the user enters a Valid index
except IndexError:
    print("Error: Index out of range. Please enter a valid index.")

# Handle the ValueError case where the user enters a non-integer value
except ValueError:
    print("Invalid input. Please enter integer values only.")
