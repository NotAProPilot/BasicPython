class Student:
    """The Student class.

    Attributes:
        name: A string indicating the name of the student.
        age: An integer indicating the age of a student.
        hobbies: A list of strings representing the student's hobbies.
        friends: A list of Student objects representing the student's friends.
    """

    def __init__(self, input_name, input_age):
        """Initialize the Student instance.

        Args:
            input_name: Defines the name of the current instance.
            input_age: Defines the age of the current instance.
        """
        self.name = input_name
        self.age = input_age
        self.hobbies = []
        self.friends = []

    def introducing(self):
        """Making an instance introduce himself/herself.

        Args:
            self: The Student instance.
        """
        print(f"Hi, my name is {self.name}, and I'm {self.age} years old. My hobbies are {', '.join(self.hobbies)}.")

    def making_friends(self, other):
        """Students can make friends with each other if they share at least one common hobby.

        Args:
            self: The Student instance.
            other: The Student instance to potentially become friends with.
        """
        common_hobbies = [hobby for hobby in self.hobbies if hobby.lower() in other.hobbies]
        if common_hobbies:
            self.friends.append(other)
            other.friends.append(self)

# Initialize Student 1 and hobbies list
student1 = Student("Adam", 5)
hobbies_student_1 = ["Gaming", "cooking", "wrestling"]
for hobby in hobbies_student_1:
    student1.hobbies.append(hobby)

# Initialize Student 2 and hobbies list
student2 = Student("Eva", 6)
hobbies_student_2 = ["cooking", "Killing", "Torturing"]
for hobby in hobbies_student_2:
    student2.hobbies.append(hobby)

# Make students introduce themselves
student1.introducing()
student2.introducing()

# Make students become friends based on common hobbies
student1.making_friends(student2)

# Print the list of friends for student 1
print(f"{student1.name}'s friends:", [friend.name for friend in student1.friends])
