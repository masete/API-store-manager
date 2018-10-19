
from flask import request, jsonify
from flask.views import MethodView
from API.models.ProductsModel import ProductsModel

class ProductsController(MethodView):

    def get(self, product_id = None):
        if product_id == None:
            return jsonify(ProductsModel.getProducts()), 200

        return ProductsModel.getProducts(product_id)    
    def post(self):
        postProduct = request.get_json()
        
        if postProduct['product_id'] != "" and postProduct['product'] != "" and postProduct['price']:
            if isinstance(postProduct['product_id'], int) and isinstance(postProduct['price'], int):
                if not isinstance(postProduct['product'], str):
                    return jsonify({"status":"Bad Request","message": "Products field should be a string"}), 400
                else:
                    prodObject = {
                        "product_id": postProduct['product_id'],
                        "product": postProduct['product'],
                        "price": postProduct['price'],
                    }
                    return ProductsModel.createProduct(prodObject)
                    
            else:
                return jsonify({"status":"Bad Request","message": "Products id and price field should be an integer"}), 400
        else:
            return jsonify({"status":"Bad Request","message": "No field is expected to be empty"}), 400    