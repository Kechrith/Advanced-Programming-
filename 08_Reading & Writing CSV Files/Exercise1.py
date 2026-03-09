import csv

with open("./Chapter8/Scores.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    data = []

    for row in reader:
        id = row[0]
        name = row[1]
        score = int(row[2])

        if score > 85:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 50:
            grade = "C"
        else:
            grade = "F"

        data.append([id, name, score, grade])

with open("Scores_with_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Score", "Grade"])
    writer.writerows(data)

print("File created successfully.")