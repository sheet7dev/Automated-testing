from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Order import *


class TestGetCustomerOrders(unittest.TestCase):

    @patch.object(Storage, 'getOrders')
    def test_get_customer_orders(self, mock):
        mock.return_value = [Order(1, 1), Order(2, 1), Order(3, 3)]
        self.assertEqual(self.service.getCustomerOrders(1), [mock.return_value[0], mock.return_value[1]])

    @patch.object(Storage, 'getOrders')
    def test_get_customer_orders_is_orders_instance_of_list(self, mock):
        mock.return_value = [Order(1, 1), Order(2, 1), Order(3, 3)]
        self.assertIsInstance(self.service.getCustomerOrders(1), list)

    @patch.object(Storage, 'getOrders')
    def test_get_customer_orders_empty_list_return(self, mock):
        mock.return_value = [Order(1, 1), Order(2, 1), Order(3, 3)]
        self.assertEqual(self.service.getCustomerOrders(4), [])

    @patch.object(Storage, 'getOrders')
    def test_get_customer_orders_empty_list_check_if_not_none(self, mock):
        mock.return_value = [Order(1, 1), Order(2, 1), Order(3, 3)]
        self.assertIsNotNone(self.service.getCustomerOrders(4), [])

    @patch.object(Storage, 'getOrders')
    def test_get_customer_orders_not_provide_list_of_orders(self, mock):
        mock.return_value = None
        with self.assertRaises(Exception):
            self.service.getCustomerOrders(3)

    def test_get_customer_orders_assert_called_with_magickmock(self):
        self.service.storage.getOrders = MagicMock(name='getOrders')
        self.service.storage.getOrders.return_value = [Order(1, 1)]
        self.service.getCustomerOrders(1)
        self.service.storage.getOrders.assert_called_once()

    def test_get_customer_orders_called_with_defined_customer_id(self):
        self.service.getCustomerOrders = MagicMock(name='getCustomerOrders')
        customer_id = 2
        self.service.getCustomerOrders(customer_id)
        self.service.getCustomerOrders.assert_called_with(customer_id)

    def setUp(self):
        self.service = Service()


if __name__ == "__main__":
    unittest.main()