class SearchByName:
    def __init__(self):
        pass

    def searching(self, products, search_params):
        name = search_params['name']
        result = [product for product in products if product.name == name]
        return result