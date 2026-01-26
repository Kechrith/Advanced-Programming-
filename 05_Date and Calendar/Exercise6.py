"""
Ask the user to enter two dates, and count the number of workdays (Mon–Fri) between the two dates.
"""

import datetime 

# Ask user to input start date in YYYY-MM-DD format
user_enter_start_date = input("Enter start date (YYYY-MM-DD): ")

# Ask user to input end date in YYYY-MM-DD format
user_enter_end_date = input("Enter end date (YYYY-MM-DD): ")

# Convert the input strings into date objects
start_date = datetime.datetime.strptime(user_enter_start_date, "%Y-%m-%d").date()
end_date = datetime.datetime.strptime(user_enter_end_date, "%Y-%m-%d").date()

# Variable to store total number of working days
work_day = 0

# Start counting from the start date
current_date = start_date

# Loop through every day until reaching the end date
while current_date <= end_date:
    if current_date.weekday() < 5:
        work_day += 1   
    current_date += datetime.timedelta(days=1)

# Display total working days
print("Total work:", work_day)

