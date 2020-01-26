from Invoices import Invoices
from BalanceStrategy import DebtorBalanceStrategy, CreditorBalanceStrategy

class Supplier:
    def __init__(self,name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def create_supplier(name, phone_number):
        return Supplier(name, phone_number)

    def calculate_balance(self,invoices,balance_strategy_obj):
        my_invoices = invoices.get_invoices_per_supplier(self)
        return balance_strategy_obj.balance(my_invoices)

    def calculate_total_balance(self):
        debtor_amount = self.calculate_balance(DebtorBalanceStrategy)
        creditor_amount = self.calculate_balance(CreditorBalanceStrategy)
        return debtor_amount - creditor_amount
