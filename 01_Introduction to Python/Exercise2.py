"""If the user enters 1, then it should ask them for the length of one of its sides and display the area. If 
they select 2, it should ask for the base and height of the triangle and display the area. If they type in 
anything else, it should give them a suitable error message."""

print("="*30)
# display the following message
print("1. Square")
print("2. Triangle")

#get user input
user = input("Enter number: ").strip()

#option for user to calculate
if user == "1":
    print("You chose to calculate Square: ")
    length = float(input("Enter length: "))
    area = length * length
    print(f"The area of square is: {area:.2f}")

elif user == "2":
    print("You cose to calculate Triangle: ")
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print(f"The area of Triangle is: {area:.2f}")

else:
    print("Please Enter Number..!!")

