from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Customer import *


class TestDeleteCustomer(unittest.TestCase):

    @patch.object(Storage, 'deleteCustomer')
    def test_delete_customer_true_output(self, mock):
        mock.return_value = True
        self.assertEqual(self.service.deleteCustomer(1), 'customer with id: 1 deleted')

    @patch.object(Storage, 'deleteCustomer')
    def test_delete_customer_false_output(self, mock):
        mock.return_value = False
        with self.assertRaises(Exception):
            self.service.deleteCustomer(1)

    @patch.object(Storage, 'deleteCustomer')
    def test_delete_customer_len_of_data(self, mock):
        mock.return_value = True
        self.service.deleteCustomer(1)
        self.service.storage.data = []
        self.assertEqual(len(self.service.storage.data), 0)

    @patch.object(Storage, 'deleteCustomer')
    def test_delete_customer_called_with(self, mock):
        self.service.deleteCustomer(123)
        mock.assert_called_with(123)

    def test_delete_customer_assert_called_with_magickmock(self):
        self.service.storage.deleteCustomer = MagicMock(name='deleteCustomer')
        customer_id = 1
        self.service.deleteCustomer(customer_id)
        self.service.storage.deleteCustomer.assert_called_with(customer_id)

    def setUp(self):
        self.service = Service()
        self.service.storage.data = [Customer(1, 'Kamil', 'kamyk@buziaczek.pl')]


if __name__ == "__main__":
    unittest.main()