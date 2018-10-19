from flask import request, jsonify
from flask.views import MethodView
from API.models.SalesModel import SalesModel

class SalesController(MethodView):

    def get(self, sales_id = None):
        if sales_id == None:
            return jsonify(SalesModel.getSales()), 200
