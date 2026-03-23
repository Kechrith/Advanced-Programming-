"""
Write  a  test  program  that  creates  two  students,  student1  and  student2.  The  student1  takes  two 
subjects,  and  the  student2  takes  three  subjects.  Display  the  students  and  their  subjects.
"""
# Subject class
class Subject:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def displaySubjectDetail(self):
        print("-", self.name + ",", self.score)


# Student class
class Student:
    def __init__(self, id, name, subjects):
        self.id = id
        self.name = name
        self.subjects = subjects   # list of Subject objects

    def displaySubjects(self):
        print(self.id + ",", self.name + ":")
        for sub in self.subjects:
            sub.displaySubjectDetail()


# -------- TEST PROGRAM --------

# Student 1 subjects
s1_sub1 = Subject("Java", 85)
s1_sub2 = Subject("OOAD", 70)

student1 = Student("001", "John Smith", [s1_sub1, s1_sub2])

# Student 2 subjects
s2_sub1 = Subject("Java", 90)
s2_sub2 = Subject("OOAD", 82)
s2_sub3 = Subject("Web", 75)

student2 = Student("002", "Lucy Brown", [s2_sub1, s2_sub2, s2_sub3])

# Display result
student1.displaySubjects()
student2.displaySubjects()