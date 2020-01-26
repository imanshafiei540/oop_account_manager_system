from ProductSpec import ProductSpec
from Product import Product


class Inventory:
    def __init__(self, search=None):
        self.search_obj = search
        self.products = []

    def add_product(self, name, price, numbers, sale_price, product_type):
        product_spec_obj = ProductSpec.create(sale_price, product_type)
        product_obj = Product.create(name, price, numbers, product_spec_obj)
        self.products.append(product_obj)
        return product_obj

    def get_product(self, name):
        objects = [product for product in self.products if product.name == name]
        return objects[0]

    def delete_product(self, name):
        objects = self.get_product(name)
        self.products.remove(objects[0])

    def search(self, search_strategy, search_params):
        search_strategy.searching(self.products, search_params)
    

