"""
Routes module to handle request urls
"""

from API.controllers.ProductsController import ProductsController      

class Routes:
    """
    Class to generate urls
    """
    @staticmethod
    def generate(app):
       
        
        app.add_url_rule('/api/v1/products/', view_func=ProductsController.as_view('get_products'), methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/products/<int:product_id>', view_func=ProductsController.as_view('get_single_product'), methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/products/', view_func=ProductsController.as_view('post_products'), methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v1/sales/', view_func=SalesController.as_view('get_sales'), methods=['GET'], strict_slashes=False)