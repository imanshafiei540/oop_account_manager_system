from Supplier import Supplier

class Suppliers:
    def __init__(self):
        self.suppliers=[]

    def delete_supplier(self,supplierObj):
        self.suppliers.remove(supplierObj)

    def add_supplier(self,name, phonenumber):
        self.suppliers.append(Supplier.create_supplier(name, phonenumber))

    def update_supplier(self):
        pass
