import unittest
import requests
import allure


@allure.feature('Test POST')
@allure.severity(allure.severity_level.BLOCKER)
class TestProductsApiPOST(unittest.TestCase):
    BASE_URL = "https://localhost:5007/swagger/index.html"

    def test_create_product(self):
        url = f"{self.BASE_URL}/products"
        product_data = {
            "name": "Sample Product",
            "description": "This is a sample product",
            "price": 19.99,
            "quantity": 100,
            "rating": 4
        }
        response = requests.post(url, json=product_data)

        self.assertEqual(response.status_code, 201, f"Expected status code 201 but got {response.status_code}")

        response_data = response.json()
        self.assertIn('productId', response_data, "Response should contain 'productId'")
        self.assertEqual(response_data['name'], product_data['name'], "Product name does not match")
        self.assertEqual(response_data['description'], product_data['description'], "Product description does not match")
        self.assertEqual(response_data['price'], product_data['price'], "Product price does not match")
        self.assertEqual(response_data['quantity'], product_data['quantity'], "Product quantity does not match")
        self.assertEqual(response_data['rating'], product_data['rating'], "Product rating does not match")

if __name__ == '__main__':
    unittest.main()
