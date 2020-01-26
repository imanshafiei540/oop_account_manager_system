class SearchInvoice:
    def __init__(self):
        pass

    def searching(self):
        pass

class SearchInvoiceByDate(SearchInvoice):
    def __init__(self):
        pass

    def searching(self,dict): # dict = { 'list':[] , 'start_date':'' , 'end_date':'' , 'settlement_type' : ''}
        result_list = []
        for i in invoices:
            if i.invoice_object.created_date >= dict['start_date'] and i.invoice_object.created_date <= dict['end_date']:
                result_list.append(i.invoice_object.__str__())
        return result_list

class SearchInvoiceBySettlementType(SearchInvoice):
    def __init__(self):
        pass

    def searching(self,invoices,dict):
        result_list = []
        for i in invoices:
            if i.invoice_object.settlement_type == dict['settlement_type']:
                result_list.append(i.invoice_object.__str__())
        return result_list
