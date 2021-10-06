class Student:
    count = 0
    def __init__(self, name, surname, gradebook, *args):
        self.name = name
        self.surname = surname
        self.gradebook = gradebook
        self.grades = args
        if Student.count > 20:
            quit("incorrect date")
    def avarage_score(self):
        res = sum(self.grades)/len(self.grades)
        return res
obj_1 = Student("Ira","Omel",1325,10,11,10,9,7)
print("Avarage score: " + str(obj_1.avarage_score()))



