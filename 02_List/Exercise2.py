"""
Exercise3:
Write a program that takes a list of student scores as input and outputs their corresponding grades.
"""

# Ask the user to input scores separated by spaces
print("||===============||==||===============||")
list_score = list(eval(input("Enter the score separated by spaces: ").replace(" ", ","))) 

#print the list of scores
print(list_score) 

# Use if-elif-else to determine the grade based on the score
for score in list_score: 

    if score >= 85: 
        grade = 'A' 

    elif score >= 75: 
        grade = 'B' 
        
    elif score >= 60: 
        grade = 'C' 

    else: 
        grade = 'F' 

    # Print the score and corresponding grade
    print("=> Score is :", score, ", Grade is :", grade)

print("||===============||==||===============||")