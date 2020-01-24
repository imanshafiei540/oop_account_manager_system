from InvoiceFactory import InvoiceFactory


class Invoice:
    def __init__(self, factor_number, settlement_type, tax, discount, total_price, supplier):
        self.factor_number = factor_number
        self.settlement_type = settlement_type
        self.tax = tax
        self.discount = discount
        self.total_price = total_price
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


    @staticmethod
    def create_invoice(factor_number, settlement_type, tax, discount, total_price, supplier):
        return Invoice(factor_number, settlement_type, tax, discount, total_price, supplier)

