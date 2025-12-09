"""(Find numbers divisible by 5 or 6, but not both) Write a program that displays ten numbers per line, 
all the numbers from 100 to 200 that are divisible by 5 or 6, but not both. The numbers are separated 
by exactly one space."""

count = 0 

# Loop through number from 100 to 200
for number in range(100, 201):

    # Check if the number is divisible by 5 or 6 but Not both
    if (number % 5 == 0) ^ (number % 6 == 0):

        # Print the number followed by a space, stay on the same line
        print(number, end=' ')
        count += 1

        # After printing 10 numbers, move to the next line
        if count % 10 == 0:
            print()