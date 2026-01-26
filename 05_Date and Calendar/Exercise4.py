"""
Generate random dates in a year input by the user, and display the day of the week for each.
"""
import datetime
import calendar
import random

#Ask user to input a year
year = int(input("Enter a year: "))

#Display random dates and their corresponding day names
print("\nRandom dates in", year, ":")

#Loop five times to generate 5 random dates
for i in range(5):
    month = random.randint(1, 12)
    days = calendar.monthrange(year, month)[1]
    day = random.randint(1, days)

    #Create date using year,month and day
    date = datetime.date(year, month, day)

    #Get the day name
    day_name = calendar.day_name[date.weekday()]

    #Display the date and day name
    print(date, "-", day_name)

