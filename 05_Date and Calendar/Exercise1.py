# 1. Calculate how many days remain until the next new year (January 1, 2027)

import datetime

# get today's date
today = datetime.date.today()

# set next New Year date (Jan 1, 2027)
new_year = datetime.date(2027, 1, 1)

# calculate remaining days
remaining_days = (new_year - today).days

# display result
print("Today is:", today)
print("Next New Year is:", new_year)
print("Days remaining until New Year:", remaining_days)

