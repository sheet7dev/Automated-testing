from src.sample.Service import *
from src.sample.Storage import *
import unittest
from unittest.mock import *
from src.sample.Customer import *


class TestGetCustomer(unittest.TestCase):

    @patch.object(Storage, 'getCustomers')
    def test_get_customer_customer_exists(self, mock):
        mock.return_value = [Customer(1, 'Kamil', 'kamyk@buziaczek.pl'), Customer(2, 'Filip', 'filetuj@filet.pl')]
        self.assertEqual(self.service.getCustomer(2), mock.return_value[1])

    @patch.object(Storage, 'getCustomers')
    def test_get_customer_not_equal_different_customer(self, mock):
        mock.return_value = [Customer(1, 'Kamil', 'kamyk@buziaczek.pl'), Customer(2, 'Filip', 'filetuj@filet.pl')]
        self.assertNotEqual(self.service.getCustomer(2), mock.return_value[0])

    @patch.object(Storage, 'getCustomers')
    def test_get_customer_not_exists(self, mock):
        mock.return_value = [Customer(1, 'Kamil', 'kamyk@buziaczek.pl'), Customer(2, 'Filip', 'filetuj@filet.pl')]
        with self.assertRaises(Exception):
            self.service.getCustomer(3)

    @patch.object(Storage, 'getCustomers')
    def test_get_customer_getCustomers_not_provide_list_of_customers(self, mock):
        mock.return_value = None
        with self.assertRaises(Exception):
            self.service.getCustomer(3)

    def test_get_customer_assert_called_with_magickmock(self):
        self.service.storage.getCustomers = MagicMock(name='getCustomers')
        self.service.storage.getCustomers.return_value = [Customer(1, 'Kamil', 'kamyk@buziaczek.pl')]
        self.service.getCustomer(1)
        self.service.storage.getCustomers.assert_called_once()

    def setUp(self):
        self.service = Service()

if __name__ == "__main__":
    unittest.main()

