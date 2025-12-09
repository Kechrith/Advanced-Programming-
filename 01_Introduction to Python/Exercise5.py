""" Create  a  variable  called  computer_num  and  set  the  value  to  50.  Ask  the  user  to  enter  a  number. 
While their guess is not the same as the computer_num value,  tell them if their guess is too low or 
too high and ask them to have another guess. If they enter the same value as computer_num, display 
the message “Well done, you took [count] attempts”. """

# Variable 
computer_num = 50 
count = 0

# Ask User to Input number 
guess = int(input("Enter a number: "))
count += 1

# Loop when the user not enter computer number
while guess != computer_num:

    # If the user enter the number lower than 50
    if guess < computer_num:
        print("Too Low")

    # If the user enter the number higher than 50 
    else:
        print("Too High")
    guess = int(input("Try again: "))
    count += 1

# When the user enter the number correct to computer number 
print("Well done, you took", count, "Attempt")