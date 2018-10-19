
from flask import request, jsonify
from flask.views import MethodView
from API.models.SalesModel import SalesModel

class SalesController(MethodView):

    def get(self, sales_id = None):
        if sales_id == None:
            return jsonify(SalesModel.getSales()), 200

        return SalesModel.getSales(sales_id)
        

    def post(self):
        postSale = request.get_json()
        
        if postSale['sales_id'] != "" and postSale['sale'] != "" and postSale['price']:
            if isinstance (postSale["sales_id"], int) and isinstance(postSale["price"], int):
                if isinstance(postSale["sale"], str):
                    saleObject = {
                        "sales_id": postSale['sales_id'],
                        "sale": postSale['sale'],
                        "price": postSale['price'],
                    }
        
                    return SalesModel.createSale(saleObject)
                else:
                    return jsonify({"status":"Bad Request","message": "A string is expected in this field"}), 400    
            else:
                return jsonify({"status":"Bad Request","message": "sales id and price field should be an integer"}), 400
        else:
            return jsonify({"status":"Bad Request","message": "No field is expected to be empty"}), 400