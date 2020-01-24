from Invoices import Invoices
from InvoicePay import InvoicePay
from InvoiceExpense import InvoiceExpense
from InvoicePurchase import InvoicePurchase

class Supplier:
    def __init__(name, phonenumber, invoice_obj=None,balance_strategy_obj=None):
        self.name = name
        self.phonenumber = phonenumber
        self.invoice_obj = invoice_obj
        self.balance_strategy_obj = balance_strategy_obj

    @staticmethod
    def create_supplier(name, phonenumber, invoice_obj=None, balance_strategy_obj=None):
        return Supplier(name, phonenumber, invoice_obj, balance_strategy_obj)

    def calculate_balance(self,balance_strategy_obj):
        # call a function from invoice that get supplier object and return its invoices
        my_invoices = Invoices.get_invoices_per_supplier(self) # return dictionary contains of creditors and debtors invoices
        return balance_strategy_obj.balance(my_invoices)

    def calculate_total_balance(self):
        debtor_amount = calculate_balance(DebtorBalanceStrategy)
        creditor_amount = calculate_balance(CreditorBalanceStrategy)

    def get_balancestrategyobj(self,):
        return self.balance_strategy_obj

    def get_invoiceobj(self,):
        return self.invoice_obj

    def get_inventoryobj(self):
        return self.inventroy_obj

    def set_balancestrategyobj(self,balance_strategy_obj):
        self.balance_strategy_obj = balance_strategy_obj

    def set_invoiceobj(self, invoice_obj):
        self.invoice_obj = invoice_obj
