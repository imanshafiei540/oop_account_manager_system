class ProductToPurchase:
    def __init__(self, product,  price, numbers):
        self.product = product
        self.price = price
        self.numbers = numbers

    def set_product(self, product):
        self.product = product

    def set_price(self, price):
        self.price = price

    def set_numbers(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return str(self.product)




