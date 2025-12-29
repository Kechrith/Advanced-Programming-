"""
Write a program to transform the dictionary so that it group data by projects instead:"""

# Dictionary 
students = {
    "Jonh" : {"Math": 20, "Chemistry": 10},
    "Lucy" : {"Math": 10, "Chemistry": 30} 
}

# Transform Dictionary group it by subject instead:
subjects = {}

for student_name, student_subjects in students.items():
    for subject, grade in student_subjects.items():
        if subject not in subjects:
            subjects[subject] = {}
        
        subjects[subject][student_name] = grade

print(subjects)