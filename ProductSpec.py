from SalePrice import SalePrice
from ProductType import ProductType


class ProductSpec:
    def __init__(self, sale_price, product_type):
        self.specs = {'sale_price': sale_price,
                      'product_type': product_type}

    def set_properties(self, sale_price=None, product_type=None):
        if sale_price:
            self.specs['sale_price'] = sale_price
        if product_type:
            self.specs['product_type'] = product_type

        return self.specs

    def get_properties(self):
        return self.specs

    @staticmethod
    def create(sale_price, product_type):
        sale_price_obj = SalePrice.create(sale_price)
        product_type_obj = ProductType.create(product_type)
        return ProductSpec(sale_price_obj, product_type_obj)
