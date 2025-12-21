"""(Guess the capitals) Write a program that stores five countries and their capital cities in a 2D list.
The  program  repeatedly  asks  the  user  to  enter  a  capital  city  for  a  country.  Upon  receiving  the  user 
input, the program reports whether the answer is correct. The user’s answer is not case sensitive. The 
program asks the user to answer all the countries’ capital cities and displays the total correct count. """

# 2D List store country and capital city 
capital_city = [
    ["Cambodia", "Phnom Penh"],
    ["China", "Beijing"],
    ["Japan", "Tokyo"],
    ["India", "Delhi"],
    ["Malaysia", "Kula Lumpur"]
]

# count how many answer are correct
correct_count = 0 

# Loop through each country and capital in the 2D list
for item in capital_city:
    country = item[0]
    capital = item[1]
    
    answer = input(f"What is the capital city of {country}: ")

    # Compare the user's answer with the correct capital
    if answer.strip().lower() == capital.lower():
        print("Your Answer is correct")
        correct_count += 1
    else: 
        print(f"The correct answer should be {capital}")

# Display the score 
print(f"The correct count is {correct_count}.")
