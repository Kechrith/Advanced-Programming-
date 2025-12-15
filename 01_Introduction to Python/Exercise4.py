"""A program ask u to calculate 1 − 2 + 3 − 4 + … + 29 − 30"""

#store the result
total = 0

# loop from 1-30
for i in range(1,31):
    if i % 2 == 0:
        total -= i
    else:
        total +=1

#display result
print("Result = ",total)