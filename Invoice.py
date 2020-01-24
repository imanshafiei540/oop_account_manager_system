import datetime


class Invoice:
    def __init__(self, factor_number, settlement_type, tax, discount, total_price, supplier):
        self.factor_number = factor_number
        self.settlement_type = settlement_type
        self.tax = tax
        self.discount = discount
        self.total_price = total_price
        self.created_date = datetime.datetime.now().date()
        self.supplier = supplier

    def set_factor_number(self, factor_number):
        self.factor_number = factor_number
        return True

    def set_settlement_type(self, settlement_type):
        self.settlement_type = settlement_type
        return True

    def set_tax(self, tax):
        self.tax = tax

    def set_discount(self, discount):
        self.discount = discount

    def set_total_price(self, total_price):
        self.total_price = total_price

    def __str__(self):
        return {
            "factor_number": self.factor_number,
            "settlement_type": self.settlement_type,
            "tax": self.tax,
            "discount": self.discount,
            "total_price": self.total_price,
            "created_date": self.created_date,
            "supplier": self.supplier
        }


    @staticmethod
    def create_invoice(factor_number, settlement_type, tax, discount, total_price, supplier):
        return Invoice(factor_number, settlement_type, tax, discount, total_price, supplier)

