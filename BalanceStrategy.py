from InvoicePay import InvoicePay
from InvoiceExpense import InvoiceExpense
from InvoicePurchase import InvoicePurchase

class BalanceStrategy:
    def __init__():
        pass

    def balance():
        pass

class DebtorBalanceStrategy(BalanceStrategy):
    def __init__():
        pass

    def balance(invoice_list):
        final_total = 0
        for i in invoice_list:
            if i is type(InvoiceExpense) or i is type(InvoicePurchase):
                final_total += i.total_price
        return final_total

class CreditorBalanceStrategy(BalanceStrategy):
    def __init__():
        pass

    def balance(invoice_list):
        final_total = 0
        for i in invoice_list:
            if i is type(InvoicePay):
                final_total += i.total_price
        return final_total
