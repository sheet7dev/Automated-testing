from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Order import *
from src.sample.Product import *


class TestDeleteProductFromOrder(unittest.TestCase):

    def test_delete_product_from_order_len_of_order_products_sub_list(self):
        self.service.getProduct = MagicMock(name='getProduct')
        self.service.getOrder = MagicMock(name='getOrder')
        self.service.getProduct.return_value = self.service.storage.data[1]
        self.service.getOrder.return_value = self.service.storage.data[2]
        # self.service.addProductToOrder(2, 1)
        self.service.getOrder.return_value.products.append(self.service.getProduct.return_value)
        result = self.service.deleteProductFromOrder(2, 1)
        self.assertEqual(len(result.products), 0)

    def test_delete_product_from_order_product_not_exist_in_order_products(self):
        self.service.getProduct = MagicMock(name='getProduct')
        self.service.getOrder = MagicMock(name='getOrder')
        self.service.getProduct.side_effect = self.service.storage.data[1]
        self.service.getOrder.return_value = self.service.storage.data[2]
        with self.assertRaises(TypeError):
            self.service.deleteProductFromOrder(2, 1)

    def test_delete_product_from_order_product_not_exist(self):
        self.service.getProduct = MagicMock(name='getProduct')
        self.service.getOrder = MagicMock(name='getOrder')
        self.service.getProduct.side_effect = Exception("product not exists")
        self.service.getOrder.return_value = self.service.storage.data[2]
        with self.assertRaises(Exception):
            self.service.deleteProductFromOrder(3, 1)

    def test_delete_product_from_order_order_not_exist(self):
        self.service.getProduct = MagicMock(name='getProduct')
        self.service.getOrder = MagicMock(name='getOrder')
        self.service.getProduct.return_value = self.service.storage.data[1]
        self.service.getOrder.side_effect = Exception("order not exits")
        with self.assertRaises(Exception):
            self.service.deleteProductFromOrder(2, 3)

    def setUp(self):
        self.service = Service()
        self.service.storage.data = [Product(1, 'buty', 123.99), Product(2, 'spodnie', 69.99), Order(1, 1)]


if __name__ == "__main__":
    unittest.main()