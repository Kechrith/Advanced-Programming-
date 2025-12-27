"""Write a program to: Calculate the average rating for each language. Find the most popular language (highest average rating)"""

#Survey data 
survey = {
    "Alice": {"Python": 5, "Java": 3},
    "Jack": {"Python": 4, "C++": 5},
    "Charlie": {"Java": 4, "Python": 3}
}

#Empty dictionaries to hold totals and counts
total = {}
count = {}

#Loop through each person's survey 
for p in survey:
    for l in survey[p]:
        if l not in total:
            total[l] = survey[p][l]
            count[l] = 1
        else:
            total[l] += survey[p][l]
            count[l] += 1

#Calculate averages
for l in total:
    total[l] = total[l] / count[l]

#Print results
print("Average:", total)

#Print most popular language
print("Most popular:", max(total, key=total.get))
