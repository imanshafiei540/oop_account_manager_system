from Invoices import Invoices
from InvoicePay import InvoicePay
from InvoiceExpense import InvoiceExpense
from InvoicePurchase import InvoicePurchase
from BalanceStrategy import DebtorBalanceStrategy, CreditorBalanceStrategy

class Supplier:
    def __init__(self,name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    @staticmethod
    def create_supplier(name, phonenumber):
        return Supplier(name, phonenumber)

    def calculate_balance(self,balance_strategy_obj):
        my_invoices = Invoices.get_invoices_per_supplier(self)
        return balance_strategy_obj.balance(my_invoices)

    def calculate_total_balance(self):
        debtor_amount = self.calculate_balance(DebtorBalanceStrategy)
        creditor_amount = self.calculate_balance(CreditorBalanceStrategy)

    def get_balancestrategyobj(self):
        return self.balance_strategy_obj

    def get_invoiceobj(self):
        return self.invoice_obj

    def get_inventoryobj(self):
        return self.inventroy_obj

    def set_balancestrategyobj(self,balance_strategy_obj):
        self.balance_strategy_obj = balance_strategy_obj

    def set_invoiceobj(self, invoice_obj):
        self.invoice_obj = invoice_obj
