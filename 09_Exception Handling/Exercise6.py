"""
Define a custom exception NegativeNumberError, and write a program that raises this exception if 
the user enters a negative number.
"""
# create a custom exception class
class NegativeNumberError(Exception):
    pass

try:
    number = int(input("Enter a number: ")) 

    # check if the number is negative
    if number < 0:
        raise NegativeNumberError("Negative number is not allowed")

    # print number if valid
    print("You Entered:", number)

# handle negative number error
except NegativeNumberError as e:
    print(e)

# handle non-integer input
except ValueError:
    print("Enter a valid integer") 