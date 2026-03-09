"""
Group 9 
his program reads student scores from a CSV file, assigns grades based on scores,
and writes the results to a new CSV file with grades included.
"""
import csv

# Open the input CSV file for reading
with open("./Chapter8/Scores.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    data = []  # List to store processed data

    # Process each row in the CSV
    for row in reader:
        id = row[0]
        name = row[1]
        score = int(row[2])

        # Assign grade based on score
        if score > 85:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 50:
            grade = "C"
        else:
            grade = "F"

        data.append([id, name, score, grade])

# Write the processed data to a new CSV file
with open("Scores_with_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Score", "Grade"])  # Write header
    writer.writerows(data)  # Write all data rows

print("File created successfully.")