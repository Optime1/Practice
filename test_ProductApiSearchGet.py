import unittest
import requests
import allure


@allure.feature('Test SEARCHID')
@allure.severity(allure.severity_level.BLOCKER)
class TestProductsApiSearch(unittest.TestCase):
    BASE_URL = "https://localhost:5007/swagger/index.html"

    def test_search_products(self):
        url = f"{self.BASE_URL}/products/search"
        params = {
            "search": "Sample",
            "page": "1",
            "size": "10"
        }
        response = requests.get(url, params=params)

        self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")

        response_data = response.json()
        self.assertIn('products', response_data, "Response should contain 'products'")
        self.assertIsInstance(response_data['products'], list, "'products' should be a list")
        self.assertGreater(len(response_data['products']), 0, "Product list should not be empty")
        for product in response_data['products']:
            self.assertIn('productId', product, "Each product should contain 'productId'")
            self.assertIn('name', product, "Each product should contain 'name'")
            self.assertIn('description', product, "Each product should contain 'description'")
            self.assertIn('price', product, "Each product should contain 'price'")
            self.assertIn('quantity', product, "Each product should contain 'quantity'")
            self.assertIn('rating', product, "Each product should contain 'rating'")

if __name__ == '__main__':
    unittest.main()
