"""
Write an ATM machine program. Create four functions
"""
import csv 


# Function to check login
def login(account_no, password):
    # Open Accounts.csv in read mode
    with open("Accounts.csv", "r") as file:
        reader = csv.reader(file)   # Create reader object
        next(reader)   # Skip the header row

        # Loop through each row in the file
        for row in reader:
            # Check if account number and password match
            if row[0] == account_no and row[3] == password:
                return True  
    return False   

# Function to display the balance of the user
def display_balance(account_no):
    with open("Accounts.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)   # Skip header

        # Find the account and display balance
        for row in reader:
            if row[0] == account_no:
                print("Your balance is:", row[2])

# Function to withdraw money
def withdraw(account_no):
    # Ask user for withdrawal amount
    amount = float(input("Enter amount to withdraw: "))

    # Read all data from file into a list
    with open("Accounts.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Find the account
    for row in data:
        if row[0] == account_no:
            balance = float(row[2])

            # Check if balance is enough
            if balance >= amount:
                row[2] = str(balance - amount)   # Update new balance
                print("Withdraw successful.")
            else:
                print("Balance not enough.")

    # Write updated data back to file
    with open("Accounts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Function to deposit money
def deposit(account_no):
    # Ask user for deposit amount
    amount = float(input("Enter amount to deposit: "))

    # Read file data
    with open("Accounts.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Find the account and update balance
    for row in data:
        if row[0] == account_no:
            row[2] = str(float(row[2]) + amount)
            print("Deposit successful.")

    # Save updated balance to file
    with open("Accounts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Create Accounts.csv and write initial test data
with open("Accounts.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["account_no", "name", "balance", "password"])

    # Write 5 test accounts
    writer.writerow(["1001", "Tang Kechrith", "1000", "12345"])
    writer.writerow(["1002", "Pich Chesda", "1000", "54321"])
    writer.writerow(["1003", "Keo Sela", "1000", "6789"])
    writer.writerow(["1004", "Niem Vannra", "1000", "9876"])
    writer.writerow(["1005", "Pheng Sopanha", "1000", "0001"])

# Login system
while True:
    account_no = input("Enter account number: ")
    password = input("Enter password: ")

    # Check login
    if login(account_no, password):
        print("Login successful.")
        break
    else:
        print("Login failed. Try again.")


# ATM menu
while True:
    print("\nMenu")
    print("a. Balance")
    print("b. Withdraw")
    print("c. Deposit")
    print("d. Exit")

    choice = input("Choose option: ")

    if choice == "a":
        display_balance(account_no)

    elif choice == "b":
        withdraw(account_no)

    elif choice == "c":
        deposit(account_no)

    elif choice == "d":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")