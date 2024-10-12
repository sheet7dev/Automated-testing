from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Order import *


class TestDeleteOrder(unittest.TestCase):

    @patch.object(Storage, 'deleteOrder')
    def test_delete_order_true_output(self, mock):
        mock.return_value = True
        self.assertEqual(self.service.deleteOrder(1), 'order with id: 1 deleted')

    @patch.object(Storage, 'deleteOrder')
    def test_delete_order_false_output(self, mock):
        mock.return_value = False
        with self.assertRaises(Exception):
            self.service.deleteCustomer(1)

    @patch.object(Storage, 'deleteOrder')
    def test_delete_order_len_of_data(self, mock):
        mock.return_value = True
        self.service.deleteOrder(1)
        self.service.storage.data = []
        self.assertEqual(len(self.service.storage.data), 0)

    @patch.object(Storage, 'deleteOrder')
    def test_delete_order_called_with(self, mock):
        self.service.deleteOrder(123)
        mock.assert_called_with(123)

    def test_delete_product_assert_called_with_magickmock(self):
        self.service.storage.deleteOrder = MagicMock(name='deleteOrder')
        order_id = 1
        self.service.deleteOrder(order_id)
        self.service.storage.deleteOrder.assert_called_with(order_id)

    def setUp(self):
        self.service = Service()
        self.service.storage.data = [Order(1, 1)]


if __name__ == "__main__":
    unittest.main()