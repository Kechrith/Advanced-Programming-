"""
Ask the user for their birthdate and calculate: How many days until their next birthday, and What day 
of the week their birthday falls on this year.
"""

import calendar
import datetime

# Ask user to enter their birthday
birthday_str = input("Enter your birthday (YYY-MM-DD): ")

# Convert the input string into a date object
birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()

# Current date
today = datetime.date.today()

# Create a date for user brithday in current year
this_year = datetime.date(today.year, birthday.month, birthday.day)

# check if birthday already pass this year 
if this_year < today:
    next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)
else: 
    next_birthday = this_year

# Calculate number day until the birthday
day_until = (next_birthday - today).days

# Get weekday index of birthday this year 
day_index = this_year.weekday()
day_name = calendar.day_name[day_index]

# Display result 

print("Your next birthday is on a", day_name + ".")
print("Day until your next birthday is", day_until)