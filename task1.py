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
            raise ValueError("Incorrect date")
        elif not isinstance(length,float) and not isinstance(width,float) :
            raise TypeError("Incorrect date")
        else:
            self.length = length
            self.width = width


obj1 = Rectangle()
obj1.set_attributes(float(input("Length:")), float(input("Width:")))
print(obj1.get_attributes())
