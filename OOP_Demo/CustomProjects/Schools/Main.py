from Student import Student
from Class import Class

# Initialize Student 1 and hobbies list
student1 = Student("Adam", 5)
hobbies_student_1 = ["Gaming", "Cooking", "Wrestling"]
for hobby in hobbies_student_1:
    student1.hobbies.append(hobby)

# Initialize Student 2 and hobbies list
student2 = Student("Eva", 6)
hobbies_student_2 = ["Cooking", "Killing", "Torturing"]
for hobby in hobbies_student_2:
    student2.hobbies.append(hobby)

# Initialize Student 3 and hobbies list
student3 = Student("Taylor", 8)
hobbies_student_3 = ["Singing", "Killing", "Dancing"]
for hobby in hobbies_student_3:
    student3.hobbies.append(hobby)

# Make students introduce themselves
student1.introducing()
student2.introducing()

# Make students become friends based on common hobbies
student1.making_friends(student2)

# Print the list of friends for student 1
print(f"{student1.name}'s friends:", [friend.name for friend in student1.friends])

# Create an instance of Class
class1 = Class("Intro to Python", "6.001", 20)

# List of students to be added
students_to_be_added = [student1, student2, student3]
for student in students_to_be_added:
    class1.add_students(student)

# Represent the class instance
print(repr(class1))
