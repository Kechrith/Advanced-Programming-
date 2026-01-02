""""
Repeat  addition  quiz)  Write  a  quiz  program  to  randomly  create  a  question  and  alert  the  user  if  an 
answer is needed to be entered again
"""

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
correct_answer = number1 + number2
entered_answers = []

while True:
    user_input = input(f"What is {number1} + {number2}? ")
    
    # Check if all characters are digits
    if user_input.isdigit():
        user_answer = int(user_input)
    else:
        print("Invalid input. Please enter a positive integer.")
        continue
    
    if user_answer in entered_answers:
        print(f"You already entered {user_answer}")
        print("Wrong answer. Try again.")
        continue
    
    entered_answers.append(user_answer)
    
    if user_answer == correct_answer:
        print("You got it!")
        break
    else:
        print("Wrong answer. Try again.")