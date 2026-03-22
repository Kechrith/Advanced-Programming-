'''
Group9: Write the program to calculat the area and perimeter of
the rectangle by using class    
'''

# Create the Rectangle class that stores width and height, and calculates area and perimeter
class Rectangle:
    
    # Initialize the Rectangle object with width and height parimeters
    def __init__(self, width: float = 1, height: float = 2):
        self.width = width 
        self.height = height
    
    # Calculate the area of the rectangle
    def getArea(self):
        return self.width * self.height
    
    # Calculate the parimeter of the rectangle
    def getParimeter(self):
        return 2 * (self.width + self.height)
    
# Create the object 
R1 = Rectangle(4, 40)
R2 = Rectangle(3.5 , 35.7)

# Dispaly the area and parimeter of the rectangle 1
print("==========Rectangle1==========")
print("Widht : ", R1.width)
print("Height : ", R1.height)
print("The area of the rectangle1 is : ", R1.getArea() ,"m^2")
print("The perimeter of the rectangle is : ", R1.getParimeter() ,"m")
print("==============================")

# Dispaly the area and parimeter of the rectangle 2
print("\n==========Rectangle2==========")
print("Widht : ", R2.width)
print("Height : ", R2.height)
print("The area of the rectangle1 is : ", R2.getArea() ,"m^2")
print("The perimeter of the rectangle is : ", R2.getParimeter() ,"m")
print("==============================")