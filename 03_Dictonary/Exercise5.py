"""Store id, name, salary, and department of three employees in a dictionary. Then, write a program that 
includes a menu that will allow user to select any of the following features: 
a. Display all employees 
b. Add a new employee 
c. Delete employee by id 
d. Update employee by id 
e. Search employee by id 
f. Exit the program 
When display the employee(s), the data should be arranged in a tabular format"""

employee = {
    1: {"Name": "Chan Dara", "Salary": 80, "Department": "ITE"},
    2: {"Name": "Sok Sophea", "Salary": 900, "Department": "BioE"},
    3: {"Name": "Keo Tola", "Salary": 1200, "Department": "DSE"}
}

# Repeat menu until user chooses to exit
while True:

    # Show menu options
    print("\nMENU")
    print("a. Display all employees")
    print("b. Add a new employee")
    print("c. Delete employee by id")
    print("d. Update employee by id")
    print("e. Search employee by id")
    print("f. Exit the program")

    # Get user's choice
    choice = input("Enter your choice (a-f): ")

    # display all employee 
    if choice == 'a':
        print("------------------------------------------------")
        print("ID\tName\t\tSalary\tDepartment")
        print("------------------------------------------------")
        
        # Loop through all employees and print data
        for emp_id, info in employee.items():
            print(emp_id, "\t", info["Name"], "\t", info["Salary"], "\t", info["Department"])
        print("------------------------------------------------")

    # add employee
    elif choice == 'b':
        # Get new employee details
        emp_id = int(input("Enter new employee id: "))
        name = input("Enter new employee name: ")
        salary = int(input("Enter employee salary: "))
        dept = input("Enter department: ")

        # Insert into dictionary
        employee[emp_id] = {"Name": name, "Salary": salary, "Department": dept}
        print("Employee added successfully")

    # delete employee
    elif choice == 'c':
        emp_id = int(input("Enter employee id to delete: "))

        # Check if id exists
        if emp_id in employee:
            del employee[emp_id]
            print("Employee deleted successfully")
        else:
            print("Employee ID not found")

    # update employee 
    elif choice == 'd':
        emp_id = int(input("Enter employee id to update: "))

        if emp_id in employee:
            name = input("Enter new name: ")
            salary = int(input("Enter new salary: "))
            dept = input("Enter new department: ")

            # Replace employee data
            employee[emp_id] = {"Name": name, "Salary": salary, "Department": dept}
            print("Employee updated successfully")
        else:
            print("Employee ID not found")

    # search employee
    elif choice == 'e':
        emp_id = int(input("Enter employee id to search: "))

        # Check if exists
        if emp_id in employee:
            info = employee[emp_id]
            print("------------------------------------------------")
            print("ID\tName\t\tSalary\tDepartment")
            print("------------------------------------------------")
            print(emp_id, "\t", info["Name"], "\t", info["Salary"], "\t", info["Department"])
            print("------------------------------------------------")
        else:
            print("Employee ID not found")

    # Exit program
    elif choice == 'f':
        print("Exiting program...")
        break

    # Invalid choice 
    else:
        print("Invalid choice. Please select a, b, c, d, e, or f.")