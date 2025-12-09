"""write a program that calcultate 
the energy needed to heat water from an initial temperature to a final temperature"""


print("==========Calculate the energy ==============")
M = float(input("Enter weight of water in kilogram: "))
T0= float(input("Enter Initial temerature: "))
T1 = float(input("Enter Final Temperature: "))
Q = M * (T1 - T0) * 4184
print("The formula to compute the energy is: ",Q)