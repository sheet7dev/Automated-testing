from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Customer import *


class TestAddCustomer(unittest.TestCase):

    @patch.object(Storage, 'addCustomer')
    def test_add_customer_true_output(self, mock):
        mock.return_value = True
        self.assertEqual(self.service.addCustomer(Customer(3, 'Paweł', 'pawcio@gmail.com')), 'customer has been added')

    @patch.object(Storage, 'addCustomer')
    def test_add_customer_false_output(self, mock):
        mock.return_value = False
        with self.assertRaises(Exception):
            self.service.addCustomer(Customer(3, 'Paweł', 'pawcio@gmail.com'))

    @patch.object(Storage, 'addCustomer')
    def test_add_customer_method_id_not_int(self, mock):
        mock.side_effect = TypeError('customers id must be an int')
        with self.assertRaises(TypeError):
            self.service.addCustomer(Customer('100', 'Kamil', 'kamyk@buziaczek.pl'))

    @patch.object(Storage, 'addCustomer')
    def test_add_customer_method_name_not_str(self, mock):
        mock.side_effect = TypeError('name must be a string')
        with self.assertRaises(TypeError):
            self.service.addCustomer(Customer(100, 12, 'cust@example.com'))

    @patch.object(Storage, 'addCustomer')
    def test_add_customer_method_name_empty_str(self, mock):
        mock.side_effect = ValueError('name cannot be an empty string')
        with self.assertRaises(ValueError):
            self.service.addCustomer(Customer(100, '', 'cust@example.com'))

    def test_add_customer_id_not_int_magicmock(self):
        self.service.storage.addCustomer = MagicMock(name='addCustomer', spec=Storage)
        self.service.storage.addCustomer.side_effect = TypeError('customers id must be an int')
        with self.assertRaises(TypeError):
            self.service.addCustomer(Customer('1', 'Bartek', 'example@example.com'))

    def test_add_customer_assert_called_with_magickmock(self):
        self.service.storage.addCustomer = Mock(name='addCustomer')
        customer = Customer(3, 'Paweł', 'pawcio@gmail.com')
        self.service.addCustomer(customer)
        self.service.storage.addCustomer.assert_called_with(customer)

    def test_new_customer_attribute_error_magickmock(self):
        self.service.storage.addCustomer = MagicMock(name='addCustomer', spec='Storage')
        with self.assertRaises(AttributeError):
            self.service.newCustomer()

    def setUp(self):
        self.service = Service()


if __name__ == "__main__":
    unittest.main()