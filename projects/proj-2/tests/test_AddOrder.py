from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Order import *


class TestAddOrder(unittest.TestCase):

    @patch.object(Storage, 'addOrder')
    def test_add_order_true_output(self, mock):
        mock.return_value = True
        self.assertEqual(self.service.addOrder(Order(1, 1)), 'order has been added')

    @patch.object(Storage, 'addOrder')
    def test_add_order_false_output(self, mock):
        mock.return_value = False
        with self.assertRaises(Exception):
            self.service.addProduct(Order(1, 1))

    @patch.object(Storage, 'addOrder')
    def test_add_order_order_id_not_int(self, mock):
        mock.side_effect = TypeError("order id must be an int")
        with self.assertRaises(TypeError):
            self.service.addProduct(Order('1', 1))

    @patch.object(Storage, 'addOrder')
    def test_add_order_customer_id_not_int(self, mock):
        mock.side_effect = TypeError("customer id must be an int")
        with self.assertRaises(TypeError):
            self.service.addProduct(Order(1, '1'))

    def test_add_order_assert_called_with_magickmock(self):
        self.service.storage.addOrder = MagicMock(name='addOrder')
        order = Order(1, 1)
        self.service.addOrder(order)
        self.service.storage.addOrder.assert_called_with(order)

    def setUp(self):
        self.service = Service()


if __name__ == "__main__":
    unittest.main()