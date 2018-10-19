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
        else:
            for product in ProductsModel.productsData():
                if product.get('product_id') == product_id:
                    return jsonify(product), 200
        
        return jsonify({"status":"Not Found", "message":"File doesnot exist on server"}), 404   


    @staticmethod
    def createProduct(newProduct):
        ProductsModel.productList = ProductsModel.productsData()
        newProductList = []
        ProductsModel.productList.append(newProduct)
        newProductList = ProductsModel.productList
        return jsonify({"status": "Created", "message" : "You have created a product", "product":newProduct}), 200    