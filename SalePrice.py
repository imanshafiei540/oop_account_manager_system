class SalePrice:
    def __init__(self, sale_price):
        self.sale_price = sale_price

    def get_sale_price(self):
        return self.sale_price

    def set_sale_price(self, sale_price):
        self.sale_price = sale_price
        return self.sale_price

    @staticmethod
    def create(sale_price):
        return SalePrice(sale_price)
