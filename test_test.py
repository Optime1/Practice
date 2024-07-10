import requests
import allure
from configuration import SERVICE_URL
from src.enums.global_enums import Global_Error_Messages
from swagger_server.test import BaseTestCase

@allure.feature('Test ProductApi')
@allure.story('Add and get of api')
@allure.severity(allure.severity_level.BLOCKER)
class TestDefaultController(BaseTestCase):
    def test_getting_posts(self):
        response = requests.get(url=SERVICE_URL)
        received_posts = response.json()

        assert response.status_code == 200, Global_Error_Messages.WRONG_STATUS_CODE.value
        assert len(received_posts) == 2, Global_Error_Messages.WRONG_ELEMENT_COUNT

    def test_products_post(self):
        response = self.client.open(
            '/products',
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_products_product_id_get(self):
        response = self.client.open(
            '/products/{product_id}'.format(product_id='product_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_products_product_id_put(self):
        response = self.client.open(
            '/products/{product_id}'.format(product_id='product_id_example'),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_products_search_get(self):
        urlsearch = "https://localhost:5007/api/v1/products/search"
        query_string = {'search': 'search_example',
                        'page': 'page_example',
                        'size': 'size_example'}
        response = requests.get(url=urlsearch, params=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))