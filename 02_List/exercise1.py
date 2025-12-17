"""Group 9
Write  a  program  that  first  will  read  integers  from  the  user  into  a  list  until  the  user  enters  0.  Then, 
display the list that contains no duplicate. You are allowed have only one list for this program. Hint: 
store only the new entered integer; if the entered integer already existed in the list, do not store it."""
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