"""(Find numbers divisible by 5 or 6, but not both) Write a program that displays ten numbers per line, 
all the numbers from 100 to 200 that are divisible by 5 or 6, but not both. The numbers are separated 
by exactly one space."""
count = 0 

for number in range(100, 201):
    if (number % 5 == 0) ^ (number % 6 == 0):
        print(number, end=' ')
        count += 1
        if count % 10 == 0:
            print()