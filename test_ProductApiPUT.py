import unittest
import requests
import allure


@allure.feature('Test PUT')
@allure.severity(allure.severity_level.BLOCKER)
class TestProductsApiPUT(unittest.TestCase):
    BASE_URL = "https://localhost:5007/swagger/index.html"

    def test_update_product_by_id(self):
        product_id = "12345"
        url = f"{self.BASE_URL}/products/{product_id}"
        update_data = {
            "name": "Updated Product",
            "description": "This is an updated description",
            "price": 29.99,
            "quantity": 150,
            "rating": 5
        }
        response = requests.put(url, json=update_data)

        self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")

        response_data = response.json()
        self.assertEqual(response_data['productId'], product_id, "Product ID does not match")
        self.assertEqual(response_data['name'], update_data['name'], "Updated product name does not match")
        self.assertEqual(response_data['description'], update_data['description'], "Updated product description does not match")
        self.assertEqual(response_data['price'], update_data['price'], "Updated product price does not match")
        self.assertEqual(response_data['quantity'], update_data['quantity'], "Updated product quantity does not match")
        self.assertEqual(response_data['rating'], update_data['rating'], "Updated product rating does not match")

if __name__ == '__main__':
    unittest.main()
