from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Product import *


class TestAddProduct(unittest.TestCase):

    @patch.object(Storage, 'addProduct')
    def test_add_product_true_output(self, mock):
        mock.return_value = True
        self.assertEqual(self.service.addProduct(Product(1, 'buty', 123.99)), 'product has been added')

    @patch.object(Storage, 'addProduct')
    def test_add_product_false_output(self, mock):
        mock.return_value = False
        with self.assertRaises(Exception):
            self.service.addProduct(Product(1, 'buty', 123.99))

    @patch.object(Storage, 'addProduct')
    def test_add_product_product_id_not_int(self, mock):
        mock.side_effect = TypeError("product id must be an int")
        with self.assertRaises(TypeError):
            self.service.addProduct(Product('1', 'buty', 123.99))

    @patch.object(Storage, 'addProduct')
    def test_add_product_product_name_not_str(self, mock):
        mock.side_effect = TypeError("name must be a string")
        with self.assertRaises(TypeError):
            self.service.addProduct(Product(1, 3, 123.99))

    @patch.object(Storage, 'addProduct')
    def test_add_product_product_value_not_float(self, mock):
        mock.side_effect = TypeError("value must be a float type")
        with self.assertRaises(TypeError):
            self.service.addProduct(Product(1, 'buty', '123.99'))

    @patch.object(Storage, 'addProduct')
    def test_add_product_product_value_less_than_zero(self, mock):
        mock.side_effect = ValueError("wrong value")
        with self.assertRaises(ValueError):
            self.service.addProduct(Product(1, 'buty', -32.00))

    def test_add_product_assert_called_with_magickmock(self):
        self.service.storage.addProduct = MagicMock(name='addProduct')
        product = Product(1, 'buty', 129.99)
        self.service.addProduct(product)
        self.service.storage.addProduct.assert_called_with(product)

    def setUp(self):
        self.service = Service()


if __name__ == "__main__":
    unittest.main()