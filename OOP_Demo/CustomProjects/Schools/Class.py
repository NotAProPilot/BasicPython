from Student import Student

class Class:
    """The Class class.

    Attributes:
        name (str): The name of the class.
        code (str): The class code.
        num_of_students (int): The number of students in the class.
        pass_grade (int): The passing grade for the class.
        student_list (list of Student): The list of students in the class.
        passed_students (list of Student): The list of students who have passed the class.
    """

    def __init__(self, input_name, input_code, input_number_of_students):
        """Initializes the Class instance.

        Args:
            input_name (str): The name of the class.
            input_code (str): The class code.
            input_number_of_students (int): The number of students in the class.
        """
        self.name = input_name
        self.code = input_code
        self.num_of_students = input_number_of_students
        self.pass_grade = 5
        self.student_list = []
        self.passed_students = []

    def __repr__(self):
        """Represents an instance of Class."""
        return ("This class, {name} ({code}), has {num_of_students} students. "
                "Current students are {student_list} and passed students are {passed_students}."
                .format(name=self.name, code=self.code,
                        num_of_students=self.num_of_students,
                        student_list=[student.name for student in self.student_list],
                        passed_students=[student.name for student in self.passed_students]))

    def add_students(self, student):
        """Adds students into the class if they are older than 8.

        Args:
            student (Student): The student to add to the class.
        """
        if student.age >= 8:
            self.student_list.append(student)

# Example usage:
# student3 = Student("Taylor", 8)
# hobbies_student_3 = ["Singing", "Killing", "Dancing"]
# for hobby in hobbies_student_3:
#     student3.hobbies.append(hobby)

# class1 = Class("Intro to Python", "6.001", 20)

# students_to_be_added = [student1, student2, student3]
# for student in students_to_be_added:
#     class1.add_students(student)

# print(repr(class1))
