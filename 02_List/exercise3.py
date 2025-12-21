# write a program that reads some integers between 1 and 100 separeated by a space 
num_list = []
user_input = input("Enter integers between 1 and 100 (seperated by a space): ")

# check if user input not iteger
for num_str in user_input.split(" "):
    if num_str.isdigit():
        num = int(num_str)
        if 1 <= num <= 100:
            num_list.append(num)
        else:
            print(f"Error: {num} is out of range; please enter integers between 1 and 100.")
            exit()
    else:
        print(f"Error: '{num_str}' is not a valid integer.")
        exit()

# check the number and convert it from string to integers
counted = set()
for num in num_list:
    if num not in counted:
        count = num_list.count(num)
        counted.add(num)
        if count == 1:
            print(f"{num} occurs {count} time.")
        else:
            print(f"{num} occurs {count} times.")