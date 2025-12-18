""" Write  a  program  that  reads  some  integers  between  1  and  100  separated  by  a  space  in  one  line,  and 
counts the occurrences of each """ 

numbers = list(map(int, input("Enter integers between 1 and 100: ").split()))

# Loop through numbers from 1 to 100
for i in range(1, 101):
    count = numbers.count(i)

    # Only display numbers that appear at least once
    if count > 0: 
        if count == 1:
            print(i, "Occurs", count, "time")
        else:
            print(i, "Occurs", count, "times")