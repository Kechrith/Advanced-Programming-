"""
Write a test program that will ask the user to select the menu: 
1. Circle 
2. Triangle  
After the user select the menu, ask the user to enter what needed and display the result returned by the 
function in the module.
"""

import geometrymodule

# Display menu options to the user
print("Menu:")
print("1. Circle")
print("2. Triangle")

# Ask the user to select a menu option
choice = int(input("Select a menu (1 or 2): "))

# If the user chooses Circle
if choice == 1:
    # Ask the user to enter the radius of the circle
    radius = float(input("Enter radius of the circle: "))
    # Call the function to compute area and perimeter of the circle
    area, perimeter = geometrymodule.compute_circle(radius)
    # Display the results
    print("Circle Area: ", area)
    print("Circle Perimeter: ", perimeter)

# If the user chooses Triangle
elif choice == 2:
    # Ask the user to enter the three sides of the triangle
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    # Call the function to compute area and perimeter of the triangle
    area, perimeter = geometrymodule.compute_triangle(a, b, c)
    # Display the results
    print("Triangle Area: ", area)
    print("Triangle Perimeter: ", perimeter)

# If the user enters an invalid menu option
else: 
    print("Invalid choice")