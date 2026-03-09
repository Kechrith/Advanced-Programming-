"""
For the test program, check if the Employees.csv file exists or not. If the file does not exist, create it 
by adding a header that consists of ID, Name, Gender and Salary. If the file already exists
"""

import csv 
import os.path 

filename = "Employees.csv"

# Check if Employees.csv exists
if not os.path.exists(filename):
    # Create the file if it does not exist
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file) 
        writer.writerow(["ID", "Name", "Gender", "Salary"])  
    print("File Created Successfully")

# function to add new employee
def add():
    id = input("Enter ID: ")
    name = input("Enter name: ")
    gender = input("Enter Gender: ")
    salary = input("Enter Salary: ")

    # Open file in append mode to add new employee
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id, name, gender, salary])
    print("Employee added successfully")

# Function to delete employee
def delete():
    id = input("Enter ID to delete: ")
    # Read all data from the file
    with open(filename, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        new_data = [data[0]]

    found = False

    # Loop through employee records
    for row in data[1:]:
        if row[0] != id:
            new_data.append(row)
        else:
            found = True

    # Rewrite updated data back to file
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_data)

    if found:
        print("Employee deleted successfully.")
    else:
        print("ID not found.")

# Function to search employee
def search():
    id = input("Enter ID to search: ")

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # Search employee by ID 
        for row in reader:
            if row[0] == id:
                print("Employee Found:")
                print("ID:", row[0])
                print("Name:", row[1])
                print("Gender:", row[2])
                print("Salary:", row[3])
                return

    print("Search Not Found")

# Function to display all employee
def display():
    with open(filename, "r") as file:
        reader = csv.reader(file)

        print("ID Name Gender Salary")

        next(reader) 
        for row in reader:
            print(row[0], row[1], row[2], row[3])

# Main Menu 
while True:
    print("\nMenu")
    print("a. Add a new employee")
    print("b. Delete employee by ID")
    print("c. Search employee by ID")
    print("d. Display all employees")
    print("e. Exit")

    choice = input("Choose an option: ")

    if choice == "a":
        add()
    elif choice == "b":
        delete()
    elif choice == "c":
        search()
    elif choice == "d":
        display()
    elif choice == "e":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")