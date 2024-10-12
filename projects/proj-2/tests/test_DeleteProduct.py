from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Product import *


class TestDeleteProduct(unittest.TestCase):

    @patch.object(Storage, 'deleteProduct')
    def test_delete_product_true_output(self, mock):
        mock.return_value = True
        self.assertEqual(self.service.deleteProduct(1), 'product with id: 1 deleted')

    @patch.object(Storage, 'deleteProduct')
    def test_delete_product_false_output(self, mock):
        mock.return_value = False
        with self.assertRaises(Exception):
            self.service.deleteCustomer(1)

    @patch.object(Storage, 'deleteProduct')
    def test_delete_product_len_of_data(self, mock):
        mock.return_value = True
        self.service.deleteProduct(1)
        self.service.storage.data = []
        self.assertEqual(len(self.service.storage.data), 0)

    @patch.object(Storage, 'deleteProduct')
    def test_delete_product_called_with(self, mock):
        self.service.deleteProduct(123)
        mock.assert_called_with(123)

    def test_delete_product_assert_called_with_magickmock(self):
        self.service.storage.deleteProduct = MagicMock(name='deleteProduct')
        product_id = 1
        self.service.deleteProduct(product_id)
        self.service.storage.deleteProduct.assert_called_with(product_id)

    def setUp(self):
        self.service = Service()
        self.service.storage.data = [Product(1, 'buty', 123.99)]


if __name__ == "__main__":
    unittest.main()