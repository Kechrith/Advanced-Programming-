import datetime 

user_enter_start_date = input("Enter start date (YYY-MM-DD): ")
user_enter_end_date = input("Enter end date (YYY-MM-DD): ")

start_date = datetime.datetime.strptime(user_enter_start_date, "%Y-%m-%d").date()
end_date = datetime.datetime.strptime(user_enter_end_date, "%Y-%m-%d").date()

work_day = 0

current_date = start_date
while current_date <= end_date:
    if current_date.weekday() < 5:
        work_day += 1
    current_date += datetime.timedelta(days=1)

print("Total work: ",work_day)