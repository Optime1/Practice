import unittest
import requests
import allure

@allure.feature('Test GET')
@allure.severity(allure.severity_level.BLOCKER)
class TestProductsApiGetId(unittest.TestCase):
    BASE_URL = "https://localhost:5007/swagger/index.html"

    def test_get_product_by_id(self):
        product_id = "12345"
        url = f"{self.BASE_URL}/products/{product_id}"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")

        response_data = response.json()
        self.assertEqual(response_data['productId'], product_id, "Product ID does not match")
        self.assertIn('name', response_data, "Response should contain 'name'")
        self.assertIn('description', response_data, "Response should contain 'description'")
        self.assertIn('price', response_data, "Response should contain 'price'")
        self.assertIn('quantity', response_data, "Response should contain 'quantity'")
        self.assertIn('rating', response_data, "Response should contain 'rating'")

if __name__ == '__main__':
    unittest.main()
