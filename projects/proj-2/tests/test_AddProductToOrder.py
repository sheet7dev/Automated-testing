from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Order import *
from src.sample.Product import *


class TestAddProductToOrder(unittest.TestCase):

    def test_add_product_to_order_len_of_order_products_sub_list(self):
        self.service.getProduct = MagicMock(name='getProduct')
        self.service.getOrder = MagicMock(name='getOrder')
        self.service.getProduct.return_value = self.service.storage.data[1]
        self.service.getOrder.return_value = self.service.storage.data[2]
        result = self.service.addProductToOrder(2, 1)
        self.assertEqual(len(result.products), 1)

    def test_add_product_to_order_product_not_exist(self):
        self.service.getProduct = MagicMock(name='getProduct')
        self.service.getOrder = MagicMock(name='getOrder')
        self.service.getProduct.side_effect = Exception('product not exists')
        self.service.getOrder.return_value = self.service.storage.data[2]
        with self.assertRaises(Exception):
            self.service.addProductToOrder(3, 1)

    def test_add_product_to_order_order_not_exist(self):
        self.service.getProduct = MagicMock(name='getProduct')
        self.service.getOrder = MagicMock(name='getOrder')
        self.service.getProduct.return_value = self.service.storage.data[1]
        self.service.getOrder.side_effect = Exception('order not exists')
        with self.assertRaises(Exception):
            self.service.addProductToOrder(2, 54)

    def test_add_product_to_order_many_times(self):
        self.service.getProduct = MagicMock(name='getProduct')
        self.service.getOrder = MagicMock(name='getOrder')
        self.service.getProduct.return_value = self.service.storage.data[1]
        self.service.getOrder.return_value = self.service.storage.data[2]
        self.service.addProductToOrder = MagicMock(name='addProductToOrder')
        self.service.addProductToOrder(1, 1)
        self.service.addProductToOrder(1, 1)
        self.service.addProductToOrder(1, 1)
        calls = [call(1, 1), call(1, 1), call(1, 1)]
        self.service.addProductToOrder.assert_has_calls(calls)

    def setUp(self):
        self.service = Service()
        self.service.storage.data = [Product(1, 'buty', 123.99), Product(2, 'spodnie', 69.99), Order(1, 1)]


if __name__ == "__main__":
    unittest.main()