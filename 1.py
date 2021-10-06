class Product:
    'a class that describes a product '
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions


class Customer:
    'a class that describes a customer'
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def output(self):
        return f'Customer:{self.surname} {self.name} {self.patronymic}, {self.phone}\n'


class Order(Customer, Product):
    'class that contain date about customer and product'
    sum = 0

    def __init__(self, surname, name, patronymic, phone):
        Customer.__init__(self, surname, name, patronymic, phone)

    def buy_product(self, price, description, dimensions):
        Product.__init__(self, price, description, dimensions)
        self.sum += self.price

    def total_value(self):
        return self.sum

    def get(self):
        return f'{Customer.output(self)}'


order_1 = Order("Omel", "Ira", "Romanivna", 3809702)
order_1.buy_product(10, "Cup", 21)
order_1.buy_product(200, "Book", 21)
order_2 = Order("Dovga", "Oksana", "Igorivna", 38097)
order_2.buy_product(111, "Notebook", 21)
order_2.buy_product(22, "Pencil", 21)
print(order_1.get() + "Total value 1 order: " + str(order_1.total_value()))
print(order_2.get() + "Total value 2 order: " + str(order_2.total_value()))
