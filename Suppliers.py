from Supplier import Supplier

class Suppliers:
    def __init__(self):
        self.suppliers=[]

    def delete_supplier(self,supplierObj):
        self.suppliers.remove(supplierObj)

    def add_supplier(self):
        self.suppliers.append(Supplier.create_supplier())

    def update_supplier(self):
        pass
