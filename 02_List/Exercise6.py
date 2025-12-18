"""(Guess the capitals) Write a program that repeatedly asks the user to enter a capital city for a country. 
Upon  receiving  the  user  input,  the  program  reports  whether  the  answer  is  correct.  Assume  that  10 
countries  and their capital cities  are  stored in a 2D  list. The program asks  the user to answer all the 
countries’  capital  cities and displays the total correct count. The user’s  answer is  not  case sensitive. 
The  questions  are  randomly  displayed."""
import random 

# List of country and capital city 
country_list = [
    ["Cambodia", "Phnom Penh"],
    ["Ukraine", "Kyiv"],
    ["China", "Beijing"],
    ["Japan", "Tokyo"],
    ["India", "Delhi"],
    ["Malaysia", "Kuala Lumpur"],
    ["Russia", "Moscow"],
    ["United States Of America", "Washington"],
    ["Vietnam", "Hanoi"],
    ["Indonesia", "Jakarta"]
]

# Random question 
random.shuffle(country_list)

correct_count = 0

# Asking the question
for country, city in country_list:
    answer = input(f"What is the capital city of {country} : ")

    # # Case-insensitive comparison
    if answer.lower() == city.lower():
        print("Your Answer is correct")
        correct_count += 1
    else:
        print("The correct answer should be", city)

# Print the correct score 
print("The correct count is: ", correct_count)