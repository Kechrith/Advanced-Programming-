#A program ask the use to enter a month and year to count saturday
import calendar

#ask user for input month and year
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

#get calendar for the month
cal = calendar.monthcalendar(year, month)

count_saturday = 0 

#saturday is index 5 ["mon",......,["sat"],["sun"]]
for week in cal:
    if week[5] != 0:
        count_saturday += 1

#print total of saturday
print("Total of Saturdays: ", count_saturday)
