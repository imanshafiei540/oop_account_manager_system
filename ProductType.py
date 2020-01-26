class ProductType:
    def __init__(self, product_type):
        self.product_type = product_type

    def get_product_type(self):
        return self.product_type

    def set_product_type(self, product_type):
        self.product_type = product_type
        return self.product_type

    def __str__(self):
        return self.product_type

    @staticmethod
    def create(product_type):
        return ProductType(product_type)
