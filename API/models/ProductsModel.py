from flask import jsonify

class ProductsModel:

    productList = []

    @staticmethod
    def productsData():
        return [
            {
                "product_id": 1,
                "product": "samsung",
                "price": 34564564,
            },
            {
                "product_id": 2,
                "product": "iphone",
                "price": 34564564,
            },
            {
                "product_id": 3,
                "product": "techno",
                "price": 34564564,
            }
        ]

    @staticmethod
    def getProducts(product_id = None):
        if product_id == None:
            return ProductsModel.productsData()