"""
Write  a  program  that  asks  the  user  to  input  a  string  and  an  index.  Display  the  character  at  the 
specified index. Handle: 
- IndexError if the position is out of range. 
- ValueError if the position is not an integer.
"""

try: 
    # Input String
    text = input("Enter a string: ")

    # Input Index and convert it into Integer
    index = int(input("Enter an index: "))

    # Display 
    print("Character at index: ", text[index])

# If the user input something that can't convert to integer 
except ValueError:
    print("Error 404 not found: Index Must be Integer")

# If the index doesn't not exit in the string
except IndexError:
    print("Error 404 not found: Index is out of range")