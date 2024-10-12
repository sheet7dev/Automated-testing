from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Product import *


class TestGetProduct(unittest.TestCase):

    @patch.object(Storage, 'getProducts')
    def test_get_product_product_exists(self, mock):
        mock.return_value = [Product(1, 'buty', 123.99), Product(2, 'spodnie', 69.99)]
        self.assertEqual(self.service.getProduct(2), mock.return_value[1])

    @patch.object(Storage, 'getProducts')
    def test_get_product_not_exists(self, mock):
        mock.return_value = [Product(1, 'buty', 123.99), Product(2, 'spodnie', 69.99)]
        with self.assertRaises(Exception):
            self.service.getCustomer(3)

    @patch.object(Storage, 'getProducts')
    def test_get_product_getProducts_not_provide_list_of_products(self, mock):
        mock.return_value = None
        with self.assertRaises(Exception):
            self.service.getCustomer(3)

    def test_get_product_assert_called_with_magickmock(self):
        self.service.storage.getProducts = MagicMock(name='getProducts')
        self.service.storage.getProducts .return_value = [Product(1, 'buty', 123.99)]
        self.service.getProduct(1)
        self.service.storage.getProducts .assert_called_once()

    def setUp(self):
        self.service = Service()

if __name__ == "__main__":
    unittest.main()
