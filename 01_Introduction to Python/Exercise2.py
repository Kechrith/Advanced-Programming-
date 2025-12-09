"""Write a program to calculate the area of triangle and square"""

def show ():
    print("=" * 15)
    print("Please choose the options you want to calculate: ")
    print("1. Square")
    print("2. Triangle")
def square():
    length = float(input("Enter length sides "))
    area_square = length ** 2
    print(f"The total area of square is: {area_square}")
def triangle():
    base = float(input("Enter base: "))
    height = float(input("Enter heigth of triagnle: "))
    are_triangle = base * 0.5 * height
    print(f"The total of triangle is: {are_triangle}")

while True:
    show()
    user = int(input())
    if user == 1:
        square()
        break
    elif user == 2:
        triangle()
        break
    else:
        print("Please Enter your Option!!")
        break
