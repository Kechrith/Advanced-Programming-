"""Write a program to display Body mass index (BMI). BMI is a measure of health based on weight. It 
can be calculated by taking your weight in kilograms and dividing it by the square of your height in 
meters. The interpretation of BMI for people 16 years and older is as follows: """

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