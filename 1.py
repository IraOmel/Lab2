class Product:
    """A class that describes a product."""

    def __init__(self, price, description):
        if not isinstance(price,int) or not isinstance(description,str) :
            raise TypeError("incorrect type")
        if price < 0 or not description:
            raise ValueError("incorrect value")
        self.price = price
        self.description = description

    def __str__(self):
        return f'Product: {self.price}, {self.description}'

class Customer:
    """A class that describes a customer."""

    def __init__(self, surname, name, phone):
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(phone,int):
            raise TypeError("Incorrect type")
        if not all(letter.isalpha() for letter in surname) or not all(letter.isalpha() for letter in name):
            raise ValueError("Invalid name, surname")
        if not surname or not name or not phone:
            raise ValueError("string is empty")
        else:
          self.surname = surname
          self.name = name
          self.phone = phone


    def __str__(self):
        return f'Customer:{self.surname} {self.name}, {self.phone}'


class Order():
    """A class that contain date about customer and product."""

    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Incorrect type")
        self.customer = customer
        self.products = []

    def add_product(self, product):
        """"Function that add the product at empty list 'products'."""
        self.products.append(product)

    def del_product(self, product):
        """"Function that delete the product from list 'products'."""
        if not isinstance(product, Product):
            raise TypeError
        self.products.remove(product)

    def total_value(self):
        """"Function that count and return the total value of product in order."""
        summa = 0
        for item in self.products:
            summa += item.price
        return summa

    def __str__(self):
        return f'Order: {self.customer}, {self.products}'


customer_1 = Customer("Omel", "Ira", 3809702)
order_1 = Order(customer_1)
product_1 = Product(12, "Pen")
product_2 = Product(145, "Book")
product_3 = Product(1, "Fork")
order_1.add_product(product_1)
order_1.add_product(product_2)
order_1.add_product(product_3)
order_1.del_product(product_2)
print(customer_1)
print("Total value 1 order: " + str(order_1.total_value()))
customer_2 = Customer("Dovga", "Oksana", 38097)
order_2 = Order(customer_2)
product2_1 = Product(55, "Note")
product2_2 = Product(5, "Pencil")
order_2.add_product(product2_1)
order_2.add_product(product2_2)
print(customer_2)
print("Total value 2 order: " + str(order_2.total_value()))
