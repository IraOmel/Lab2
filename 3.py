class Student:
    """"The class Student contains the personal information about student."""

    def __init__(self, name, surname, gradebook, *args):
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError("incorrect type")
        if not all(letter.isalpha() for letter in surname) or not all(letter.isalpha() for letter in name):
            raise ValueError("Invalid name, surname")
        if not name or not surname or not gradebook:
            raise ValueError("string is empty")
        self.name = name
        self.surname = surname
        if not isinstance(gradebook, int):
            raise TypeError("incorrect type")
        self.gradebook = gradebook
        for marks in args:
            if not isinstance(marks, int):
                raise TypeError("incorrect type")
            if marks < 0 or marks > 12:
                raise ValueError("incorrect date")
        self.grades = args
        self.average = 0

    def average_score(self):
        """"A function that find the average score of each student."""
        self.average = sum(self.grades) / len(self.grades)
        return self.average

    def __lt__(self, other):
        """Method for sorting by a specific attribute."""
        return self.average_score() > other.average_score()

    def __str__(self):
        return f'Student: {self.name} {self.surname}, Grades: {self.grades}, Average score: {self.average_score()}'


class Group:
    """The class Group contains a sequence of instances of the class Student."""
    def __init__(self):
        self.students = []
        self.top_five = []

    def add_student(self, student):
        """"A function that add data about student in empty list 'students'."""
        if len(self.students) == 21:
            raise ValueError("too many students")
        if any(student.surname == i.surname for i in self.students) and any(
                student.name == i.name for i in self.students):
            raise ValueError("the same student")
        self.students.append(student)

    def del_student(self, student):
        """"A function that delete data about student from list 'students'."""
        if not isinstance(student, Student):
            raise TypeError
        self.students.remove(student)

    def list_score(self):
        """"A function that return list of the students with five
                highest average score in descending order."""
        self.students.sort()
        for i in range(5):
            self.top_five.append(self.students[i])
        return self.top_five


group = Group()
obj_1 = Student("Ira", "Omel", 1325, 10, 11, 12)
obj_2 = Student("Ira", "Mal", 1345, 12, 12, 12, 9)
obj_3 = Student("Oksana", "Dovga", 4569, 10, 10, 10, 12)
obj_4 = Student("Ann", "Lub", 4795, 1, 6, 10, 11)
obj_5 = Student("Yana", "Tel", 1225, 12, 2)
obj_6 = Student("Nik", "Rok", 4445, 7, 8, 9, 9)
obj_7 = Student("Vova", "Rois", 1111, 2, 9, 2, 9)
obj_8 = Student("Olya", "Aley", 4515, 12, 12, 12)
group.add_student(obj_1)
group.add_student(obj_2)
group.add_student(obj_3)
group.add_student(obj_4)
group.add_student(obj_5)
group.add_student(obj_6)
group.add_student(obj_7)
group.add_student(obj_8)
print("Top five of students:")
highest_score = group.list_score()
for i in range(5):
    print(highest_score[i])
