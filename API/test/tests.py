from unittest import TestCase
from flask import json
from run import APP

class Tests(TestCase):

    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def add_prod(self, product_id, product, price):
        post_prod = self.client().post(
            '/api/v1/products/',
            data=json.dumps(dict(
                product_id=product_id,
                product=product,
                price=price
            )),
            content_type='application/json'
        )
        return post_prod

    def test_add_product(self):
        post = self.add_prod(1, "samsung", 2000000)
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], 'Created')
        self.assertTrue(post_response['message'], 'You have created a product')
        self.assertTrue(post.content_type, 'application/json')
        self.assertTrue(post.status_code, 201)

    def test_product_int_error(self):
        post = self.add_prod(1, "samsung", "2000000")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], 'Bad Request')
        self.assertTrue(post_response['message'], 'Products id and price field should be an integer')
        self.assertTrue(post.content_type, 'application/json')
        self.assertTrue(post.status_code, 400)

    def test_product_value_empty(self):
        post = self.add_prod(1, "samsung", "")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], 'Bad Request')
        self.assertTrue(post_response['message'], 'No field is expected to be empty')
        self.assertTrue(post.content_type, 'application/json')
        self.assertTrue(post.status_code, 400)

    def test_get_all_products(self):
        self.add_prod(1, "samsung", 300000)
        self.add_prod(2, "Nokia", 300000)
        self.add_prod(3, "Tecno", 300000)

        request_data = self.client().get('/api/v1/products/')
        self.assertTrue(request_data.status_code, 200)

    def test_get_single_products(self):
        self.add_prod(1, "samsung", 300000)
        self.add_prod(2, "Nokia", 300000)
        self.add_prod(3, "Tecno", 300000)

        request_data = self.client().get('/api/v1/products/2/')
        self.assertTrue(request_data.status_code, 200)

    def test_no_product(self):
        self.add_prod(1, "samsung", 300000)
        self.add_prod(2, "Nokia", 300000)
        self.add_prod(3, "Tecno", 300000)

        request_data = self.client().get('/api/v1/products/10/')
        self.assertTrue(request_data.status_code, 200)




    def add_sale(self, sales_id, sale, price):
        post_sale = self.client().post(
            '/api/v1/sales/',
            data=json.dumps(dict(
                sales_id=sales_id,
                sale=sale,
                price=price
            )),
            content_type='application/json'
        )
        return post_sale

    def test_add_sale(self):
        post = self.add_sale(1, "samsung", 2000000)
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], 'Created')
        self.assertTrue(post_response['message'], 'You have created a sale')
        self.assertTrue(post.content_type, 'application/json')
        self.assertTrue(post.status_code, 201)

    def test_sale_int_error(self):
        post = self.add_sale(1, "samsung", "2000000")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], 'Bad Request')
        self.assertTrue(post_response['message'], 'sales id and price field should be an integer')
        self.assertTrue(post.content_type, 'application/json')
        self.assertTrue(post.status_code, 400)

    def test_sale_value_empty(self):
        post = self.add_sale(1, "samsung", "")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], 'Bad Request')
        self.assertTrue(post_response['message'], 'No field is expected to be empty')
        self.assertTrue(post.content_type, 'application/json')
        self.assertTrue(post.status_code, 400)

    def test_get_all_sales(self):
        self.add_sale(1, "samsung", 300000)
        self.add_sale(2, "Nokia", 300000)
        self.add_sale(3, "Tecno", 300000)

        request_data = self.client().get('/api/v1/products/')
        self.assertTrue(request_data.status_code, 200)

    def test_get_single_sale(self):
        self.add_sale(1, "samsung", 300000)
        self.add_sale(2, "Nokia", 300000)
        self.add_sale(3, "Tecno", 300000)

        request_data = self.client().get('/api/v1/sales/2/')
        self.assertTrue(request_data.status_code, 200)

        