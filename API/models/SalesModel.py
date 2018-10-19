from flask import jsonify

class SalesModel:
    
    salesList = []

    @staticmethod
    def salesData():
        return [
            { "sales_id":1,
              "sales":"sales",
              "price":74673,

            },
            {
              "sales_id":2,
              "sales":"sales",
              "price":74673,

            },
            {
              "sales_id":3,
              "sales":"sales",
              "price":74673,

            },
            {
              "sales_id":4,
              "sales":"sales",
              "price":74673,

            },
                

        ]
    @staticmethod
    def getSales(sales_id = None):
        if sales_id == None:
            return SalesModel.salesData()