from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Order import *


class TestGetOrder(unittest.TestCase):

    @patch.object(Storage, 'getOrders')
    def test_get_order_order_exists(self, mock):
        mock.return_value = [Order(1, 1), Order(2, 1)]
        self.assertEqual(self.service.getOrder(2), mock.return_value[1])

    @patch.object(Storage, 'getOrders')
    def test_get_order_not_exists(self, mock):
        mock.return_value = [Order(1, 1), Order(2, 1)]
        with self.assertRaises(Exception):
            self.service.getCustomer(3)

    @patch.object(Storage, 'getOrders')
    def test_get_order_getOrder_not_provide_list_of_orders(self, mock):
        mock.return_value = None
        with self.assertRaises(Exception):
            self.service.getCustomer(3)

    def test_get_order_assert_called_with_magickmock(self):
        self.service.storage.getOrders = MagicMock(name='getOrders')
        self.service.storage.getOrders.return_value = [Order(1,1)]
        self.service.getOrder(1)
        self.service.storage.getOrders.assert_called_once()

    def setUp(self):
        self.service = Service()

if __name__ == "__main__":
    unittest.main()
