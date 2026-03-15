'''
Group 9:
Write  a  program  that  asks  the  user  to  enter  their  age.  Handle  the  ValueError  case  where  the  user 
enters a non-integer value.
'''

# Ask teh user to enter their age
Age = (input("Enter your age: "))

# Handle the ValueError case where the user enters a non-integer value
try:
    Age = int(Age)
    print("Your age is:", Age)

except ValueError:
    print("Error: Please enter a valid integer for your age.")