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
        for i in dict['list']:
            if i.created_date >= dict['start_date'] and i.created_date <= dict['end_date']:
                result_list.append(i)
        return result_list

class SearchInvoiceBySettlementType(self,SearchInvoice):
    def __init__():
        pass

    def searching(dict):
        result_list = []
        for i in dict['list']:
            if i.settlement_type == dict['settlement_type']:
                result_list.append(i)
        return result_list
