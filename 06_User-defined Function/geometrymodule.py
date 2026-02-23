"""
Write a module that contains the following two functions: 
- compute_circle that calculates the area and perimeter of a circle, and returns the results. 
- compute_traingle that calculates the area and perimeter of a triangle, and returns the results.
"""

import math

# Function to compute the area and perimeter of a circle
def compute_circle(radius):
    # Calculate the area of the circle using the formula πr²
    area = math.pi * radius * radius
    # Calculate the perimeter (circumference) using the formula 2πr
    perimeter = 2 * math.pi * radius
    # Return both area and perimeter
    return area, perimeter 

# Function to compute the area and perimeter of a triangle
def compute_triangle(a, b, c): 
    # Calculate the perimeter by adding all three sides
    perimeter = a + b + c
    # Calculate the semi-perimeter (s)
    s = perimeter / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # Return both area and perimeter
    return area, perimeter