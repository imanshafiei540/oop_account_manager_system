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


# First Test Case Scenario
supplier = Suppliers()

# Create Two Suppliers
supplier.add_supplier('First Supplier', '09120001234')
print(' [Suppliers] : First Supplier Object is created\nSupplier Name is : ', supplier.suppliers[0].name)
print(' -------------------------------------------------- ')

supplier.add_supplier('Second Supplier', '09120002234')
print(' [Suppliers] : Second Supplier Object is created\nSupplier Name is : ', supplier.suppliers[1].name)
print(' -------------------------------------------------- ')

first_supplier = supplier.suppliers[0]
second_supplier = supplier.suppliers[1]

inventory = Inventory()

first_product = inventory.add_product('Tea', 80000, 2, None, 'consumable')
print(' [Inventory] : First Product Object is created\nName is :', first_product)
print(' -------------------------------------------------- ')

second_product = inventory.add_product('Coffee', 100000, 2, 120000, 'consumable')
print(' [Inventory] : Second Product Object is created\nName is :', second_product)
print(' -------------------------------------------------- ')


third_product = inventory.add_product('Sugar', 10000, 4, None, 'consumable')
print(' [Inventory] : Third Product Object is created\nName is :', third_product)
print(' -------------------------------------------------- ')


Invoices = Invoices()
first_invoice = Invoices.add_invoice('EXPENSE', 1, 'cash', None, None, 100000, first_supplier)
print(' [Invoices] : First Invoice Object is created\nFactor Number is :', first_invoice)
print(' -------------------------------------------------- ')

second_invoice = Invoices.add_invoice('PURCHASE', 2, 'credit', None, None, 12500000, first_supplier)
print(' [Invoices] : Second Invoice Object is created\nFactor Number is :', second_invoice)
print(' -------------------------------------------------- ')

third_invoice = Invoices.add_invoice('EXPENSE', 3, 'cash', None, None, 100000, second_supplier)
print(' [Invoices] : Third Invoice Object is created\nFactor Number is :', third_invoice)
print(' -------------------------------------------------- ')

fourth_invoice = Invoices.add_invoice('PURCHASE', 4, 'credit', None, None, 100000, second_supplier)
print(' [Invoices] : Fourth Invoice Object is created\nFactor Number is :', fourth_invoice)
print(' -------------------------------------------------- ')









