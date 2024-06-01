class Student:
    """The Student class.

    Attributes:
        name (str): The name of the student.
        age (int): The age of the student.
        hobbies (list of str): The hobbies of the student.
        friends (list of Student): The friends of the student.
    """

    def __init__(self, input_name, input_age):
        """Initializes the Student instance.

        Args:
            input_name (str): The name of the student.
            input_age (int): The age of the student.
        """
        self.name = input_name
        self.age = input_age
        self.hobbies = []
        self.friends = []

    def introducing(self):
        """Makes the instance introduce itself."""
        print(f"Hi, my name is {self.name}, and I'm {self.age} years old. My hobbies are {', '.join(self.hobbies)}.")

    def making_friends(self, other):
        """Makes friends with another student if they share at least one common hobby.

        Args:
            other (Student): The other student to potentially become friends with.
        """
        common_hobbies = [hobby for hobby in self.hobbies if hobby.lower() in map(str.lower, other.hobbies)]
        if common_hobbies:
            self.friends.append(other)
            other.friends.append(self)

# Example usage:
# student1 = Student("Adam", 5)
# hobbies_student_1 = ["Gaming", "Cooking", "Wrestling"]
# for hobby in hobbies_student_1:
#     student1.hobbies.append(hobby)

# student2 = Student("Eva", 6)
# hobbies_student_2 = ["Cooking", "Killing", "Torturing"]
# for hobby in hobbies_student_2:
#     student2.hobbies.append(hobby)

# student1.introducing()
# student2.introducing()

# student1.making_friends(student2)
# print(f"{student1.name}'s friends:", [friend.name for friend in student1.friends])
