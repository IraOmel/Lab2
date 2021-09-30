class Rectangle:

    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def get_attributes(self):
        return self.perimeter(), self.area()

    def set_attributes(self, length, width):
        if length < 0.0 or length > 20.0 or width < 0.0 or width > 20.0:
            print("Incorrect date")
            quit()
        elif type(length) is float and type(width) is float:
            self.length = length
            self.width = width
        else:
            print("Incorrect date")
            quit()


obj1 = Rectangle()
obj1.set_attributes(5.0, 2.0)
print(obj1.get_attributes())
