#A program ask the user to input weight and height to calculate BMI

#input weight and height 
w = eval(input("Enter the weigh in kilogram: "))
h = eval(input("Enter the height in meter: "))

#calculate BMI
bmi = w / (h**2)

#display bmi
print("BMI = ",bmi)

#check interpretation
if bmi < 18.5:
    print("Underweight")
elif bmi <25:
    print("Normal")
elif bmi <30:
    print("Overweight")
else:
    print("Obese")