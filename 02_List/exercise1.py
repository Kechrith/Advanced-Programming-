# Group 9
# write a program to store the user input and stop when user enter 0
number = []

# Store the number for user
while True:
        num = int(input("Enter Number (0 to stop):"))

        #Stop when number 0
        if num == 0:
            break

        #filter duplicate number
        if num not in number:
            number.append(num)
    
print(number)   