from InvoicePurchase import InvoicePurchase
from InvoiceExpense import InvoiceExpense
from InvoicePay import InvoicePay


class InvoiceFactory:
    def __init__(self):
        pass

    @staticmethod
    def generate_invoice_object(invoice_type):
        if invoice_type == "PURCHASE":
            return InvoicePurchase
        elif invoice_type == "EXPENSE":
            return InvoiceExpense
        elif invoice_type == "PAY":
            return InvoicePay