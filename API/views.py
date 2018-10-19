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