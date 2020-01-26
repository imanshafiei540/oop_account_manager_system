class Product:
    def __init__(self, name, price, numbers, product_spec):
        self.name = name
        self.price = price
        self.numbers = numbers
        self.product_specs = product_spec

    def set_name(self, name):
        self.name = name
        return self

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = price
        return self

    def get_price(self):
        return self.price

    def set_number(self, numbers):
        self.numbers = numbers
        return self

    def get_numbers(self):
        return self.numbers

    def get_specs(self):
        return self.product_specs

    def __str__(self):
        return self.name

    @staticmethod
    def create(name, price, numbers, product_spec_obj):
        return Product(name, price, numbers, product_spec_obj)

