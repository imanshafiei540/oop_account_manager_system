class InvoiceExpense:
    def __init__(self, invoice_object):
        self.invoice_object = invoice_object

    @staticmethod
    def create_invoice(invoice_object):
        return InvoiceExpense(invoice_object=invoice_object)

    def __del__(self):
        del self.invoice_object
        return True