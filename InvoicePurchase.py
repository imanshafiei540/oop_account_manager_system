class InvoicePurchase:
    def __init__(self, invoice_object):
        self.invoice_object = invoice_object
        self.products_to_purchase = []

    @staticmethod
    def create_invoice(invoice_object):
        return InvoicePurchase(invoice_object=invoice_object)

    def set_products_to_purchase(self, list_of_products):
        self.products_to_purchase = list_of_products

    def __del__(self):
        del self.invoice_object
        return True