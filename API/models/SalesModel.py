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
        else:
            for sale in SalesModel.salesData():
                if sale.get('sales_id') == sales_id:
                    return jsonify(sale), 200
        
        return jsonify({"status":"Not Found", "message":"File doesnot exist on server"}), 404    


    @staticmethod
    def createSale(newSale):
        SalesModel.saleList = SalesModel.salesData()
        newSaleList = []
        SalesModel.saleList.append(newSale)
        newSalesList = SalesModel.saleList
        return jsonify({"status": "Created", "message" : "You have created a sale", "sale":newSale}), 200



