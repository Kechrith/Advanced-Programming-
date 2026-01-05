'''
Make another quiz program that asks five questions by randomly generating two integer 
numbers between 10 to 20 to make the question (What is [num1] + [num2]?).
'''
import random

count = 0
print("========== Welcome to the Math Quiz! ==========")

# For question1 
Q1_Number1 = random.randint(10, 20)
Q1_Number2 = random.randint(10, 20)
Question1 = int(input("Question1: What is " + str(Q1_Number1) + " + " + str(Q1_Number2) + "? "))

# For question2
Q2_Number1 = random.randint(10, 20)
Q2_Number2 = random.randint(10, 20)
Question2 = int(input("Question2: What is " + str(Q2_Number1) + " - " + str(Q2_Number2) + "? "))

# For question3
Q3_Number1 = random.randint(10, 20)
Q3_Number2 = random.randint(10, 20)
Question3 = int(input("Question3: What is " + str(Q3_Number1) + " / " + str(Q3_Number2) + "? "))

# For question4
Q4_Number1 = random.randint(10, 20)
Q4_Number2 = random.randint(10, 20)
Question4 = int(input("Question4: What is " + str(Q4_Number1) + " * " + str(Q4_Number2) + "? "))

# For question5
Q5_Number1 = random.randint(10, 20)
Q5_Number2 = random.randint(10, 20)
Question5 = int(input("Question5: What is " + str(Q5_Number1) + " / " + str(Q5_Number2) + "? "))

# Check total correct answers
if Question1 == (Q1_Number1 + Q1_Number2):
    count += 1
if Question2 == (Q2_Number1 - Q2_Number2):
    count += 1
if Question3 == (Q3_Number1 / Q3_Number2):
    count += 1
if Question4 == (Q4_Number1 * Q4_Number2):
    count += 1
if Question5 == (Q5_Number1 / Q5_Number2):
    count += 1

print()
# total correct answers
print("You get", count, "correct answers out of 5. The detail is below:")
print()  

# Check answers the questions1
if Question1 == (Q1_Number1 + Q1_Number2):
    print("Question1:",(Q1_Number1),"+",(Q1_Number2),"=",(Question1), "Correct✅")
    count += 1
else:
    print("Question1:",(Q1_Number1),"+",(Q1_Number2),"=",(Question1)," Incorrect❌. The answer is", (Q1_Number1 + Q1_Number2))

# Check answers the questions2
if Question2 == (Q2_Number1 - Q2_Number2):
    print("Question2:",(Q2_Number1),"-",(Q2_Number2),"=",(Question2), "Correct✅")
    count += 1
else:
    print("Question2:",(Q2_Number1),"-",(Q2_Number2),"=",(Question2)," Incorrect❌. The answer is", (Q2_Number1 - Q2_Number2))

# Check answers the questions3
if Question3 == (Q3_Number1 / Q3_Number2):
    print("Question3:",(Q3_Number1),"/",(Q3_Number2),"=",round((Question3), 2), "Correct✅")
    count += 1
else:
    print("Question3:",(Q3_Number1),"/",(Q3_Number2),"=",round((Question3), 2)," Incorrect❌. The answer is", round((Q3_Number1 / Q3_Number2),2)) 

# Check answers the questions4
if Question4 == (Q4_Number1 * Q4_Number2):
    print("Question4:",(Q4_Number1),"*",(Q4_Number2),"=",(Question4), "Correct✅")
    count += 1
else:
    print("Question4:",(Q4_Number1),"*",(Q4_Number2),"=",(Question4)," Incorrect❌. The answer is", (Q4_Number1 * Q4_Number2))

# Check answers the questions5
if Question5 == (Q5_Number1 / Q5_Number2):    
    print("Question5:",(Q5_Number1),"/",(Q5_Number2),"=",round((Question5), 2), "Correct✅")
    count += 1  
else:
    print("Question5:",(Q5_Number1),"/",(Q5_Number2),"=",round((Question5), 2)," Incorrect❌. The answer is", round((Q5_Number1 / Q5_Number2),2))
