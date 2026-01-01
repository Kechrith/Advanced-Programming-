'''
Group 9
Randomly  generate  a  number  between  1  and  6.  Ask  the  user  to  pick  a  number.  If  the  user  guess 
correctly,  display  the  message  “Well  done”,  otherwise,  display  “Incorrect”,  and  allow  the  user  to 
enter  a  second  guess.  If  the  user  guess  correctly  on  the  second  guess,  display  “Correct”,  otherwise 
display “You lose. The correct number is [random_number]”.'''

#import random module to random number
import random

#Generate random numbers between 1 and 6
num= random.randint(1,6)

#ask the player to input number
first_time = eval(input("Pick the number between 1 and 6:"))

#check if the first time is correct
if first_time == num:
    print("Well Done😍") 
#check if the first time is incorrect
else:
    print("Incorrect😒")

    #ask the player try 2nd time
    second_time = eval(input("Pick the number again between 1 and 6:"))
    #check if the player input correct number
    if second_time == num:
        print("Correct🤩")
    #check if the player input incorrect number
    else:
        print("You lose!😓 The correct number is:", num)