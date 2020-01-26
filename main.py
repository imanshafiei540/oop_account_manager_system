from BalanceStrategy import BalanceStrategy
from Inventory import Inventory
from Invoice import Invoice
from InvoiceExpense import InvoiceExpense
from InvoiceFactory import InvoiceFactory
from InvoicePay import InvoicePay
from InvoicePurchase import InvoicePurchase
from Invoices import Invoices
from Product import Product
from ProductSpec import ProductSpec
from ProductToPurchase import ProductToPurchase
from ProductType import ProductType
from SalePrice import SalePrice
from SearchByName import SearchByName
from SearchInvoice import SearchInvoice
from SearchProductStrategy import SearchProductStrategy
from Supplier import Supplier
from Suppliers import Suppliers


class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


# First Test Case Scenario
supplier = Suppliers()

# Create Two Suppliers
supplier.add_supplier('First Supplier', '09120001234')
print(bcolors.OKGREEN + bcolors.BOLD +' [Suppliers] : First Supplier Object is created\nSupplier Name is : ', supplier.suppliers[0].name)
print(bcolors.ENDC + ' -------------------------------------------------- ')

supplier.add_supplier('Second Supplier', '09120002234')
print(bcolors.OKGREEN + bcolors.BOLD + ' [Suppliers] : Second Supplier Object is created\nSupplier Name is : ', supplier.suppliers[1].name)
print(bcolors.ENDC + ' -------------------------------------------------- ')

first_supplier = supplier.suppliers[0]
second_supplier = supplier.suppliers[1]

inventory = Inventory()

first_product = inventory.add_product('Tea', 80000, 2, None, 'consumable')
print(bcolors.OKGREEN + bcolors.BOLD + ' [Inventory] : First Product Object is created\nName is :', first_product)
print(bcolors.ENDC + ' -------------------------------------------------- ')

second_product = inventory.add_product('Coffee', 100000, 2, 120000, 'consumable')
print(bcolors.OKGREEN + bcolors.BOLD + ' [Inventory] : Second Product Object is created\nName is :', second_product)
print(bcolors.ENDC + ' -------------------------------------------------- ')


third_product = inventory.add_product('Sugar', 10000, 4, None, 'consumable')
print(bcolors.OKGREEN + bcolors.BOLD + ' [Inventory] : Third Product Object is created\nName is :', third_product)
print(bcolors.ENDC + ' -------------------------------------------------- ')


Invoices = Invoices()
first_invoice = Invoices.add_invoice('EXPENSE', 1, 'cash', 0, 0, 100000, first_supplier)
print(bcolors.OKGREEN + bcolors.BOLD + ' [Invoices] : First Invoice (Expense) Object is created\nFactor Number is :', first_invoice.invoice_object)
print(bcolors.ENDC + ' -------------------------------------------------- ')


first_list_of_products = [ProductToPurchase(product=first_product, price=10000, numbers=2),
                          ProductToPurchase(product=second_product, price=20000, numbers=4)]
print(bcolors.OKGREEN + bcolors.BOLD + ' [Product To Purchase] : First Product to Purchase list of Objects is created. ')
for item in first_list_of_products:
    print(item)
print(bcolors.ENDC + ' -------------------------------------------------- ')


second_invoice = Invoices.add_invoice('PURCHASE', 2, 'credit', 0, 0, 100000, first_supplier)
second_invoice.set_products_to_purchase(first_list_of_products)
print(bcolors.OKGREEN + bcolors.BOLD + ' [Invoices] : Second Invoice (Purchase) Object is created\nFactor Number is :', second_invoice.invoice_object)
print(bcolors.ENDC + ' -------------------------------------------------- ')

third_invoice = Invoices.add_invoice('EXPENSE', 3, 'credit', 0, 0, 100000, second_supplier)
print(bcolors.OKGREEN + bcolors.BOLD + ' [Invoices] : Third Invoice Object is created\nFactor Number is :', third_invoice.invoice_object)
print(bcolors.ENDC + ' -------------------------------------------------- ')


second_list_of_products = [ProductToPurchase(product=second_product, price=20000, numbers=4),
                          ProductToPurchase(product=third_product, price=30000, numbers=6)]
print(bcolors.OKGREEN + bcolors.BOLD + ' [Product To Purchase] : Second Product to Purchase list of Objects is created. ')
for item in second_list_of_products:
    print(item)
print(bcolors.ENDC + ' -------------------------------------------------- ')


fourth_invoice = Invoices.add_invoice('PURCHASE', 4, 'credit', 0, 0, 260000, second_supplier)
fourth_invoice.set_products_to_purchase(second_list_of_products)
print(bcolors.OKGREEN + bcolors.BOLD + ' [Invoices] : Fourth Invoice Object is created\nFactor Number is :', fourth_invoice.invoice_object)
print(bcolors.ENDC + ' -------------------------------------------------- ')









