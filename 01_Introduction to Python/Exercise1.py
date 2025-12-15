"""Group 9
Write a program that calculates the energy needed to heat water from an initial temperature to a final 
temperature.  Your  program  should  ask  the  user  to  enter  the  amount  of  water  in  kilograms  and  the 
initial and final temperatures of the water. The formula to compute the energy is:  
Q = M * (final_temperature – initial_temperature) * 4184  
where M is the weight of water in kilograms, temperatures are in degrees Celsius, and energy  Q is 
measured in joules."""

print("The formula to compute the energy is: ")

#Get user input
mass = float(input("Enter the weight of water in kilograms: "))

final_temp = float(input("Enter the final temperatures in Celsius: "))

initial_temp = float(input("Enter the initial temperatures in Celsius: "))

# Calculate measure in joules
Q = mass * (final_temp - initial_temp) * 4184

# Display the Result
print(f"The measure in joules is: {Q:.2f}")