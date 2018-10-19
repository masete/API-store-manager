
from flask import request, jsonify
from flask.views import MethodView
from API.models.ProductsModel import ProductsModel

class ProductsController(MethodView):

    def get(self, product_id = None):
        if product_id == None:
            return jsonify(ProductsModel.getProducts()), 200