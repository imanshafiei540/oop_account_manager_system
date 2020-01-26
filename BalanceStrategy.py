from InvoicePay import InvoicePay
from InvoiceExpense import InvoiceExpense
from InvoicePurchase import InvoicePurchase

class BalanceStrategy:
    def __init__(self):
        pass

    def balance(self):
        pass

class DebtorBalanceStrategy(BalanceStrategy):
    def __init__(self):
        pass

    def balance(self,invoice_list):
        final_total = 0
        for i in invoice_list:
            if type(i) is InvoiceExpense or type(i) is InvoicePurchase:
                if i.invoice_object.settlement_type == "credit":
                    final_total += i.invoice_object.total_price
        return final_total

class CreditorBalanceStrategy(BalanceStrategy):
    def __init__(self):
        pass

    def balance(self,invoice_list):
        final_total = 0
        for i in invoice_list:
            if type(i) is InvoicePay:
                final_total += i.invoice_object.total_price
        return final_total
