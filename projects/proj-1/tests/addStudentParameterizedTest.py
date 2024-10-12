import unittest
from parameterized import parameterized
from src.sample.sms import *


class SMSParameterized1(unittest.TestCase):

    def setUp(self):
        self.system = System()

    @parameterized.expand([
        (10, 'Marek', 'Harasim', 15, 'marek@buziaczek.pl', 'student has been added'),
        (2, 'Bartosz', 'Zmarzlik', 19, 'bartek@żużel.pl', 'student has been added'),
        (4, 'Stefan', 'Kasztan', 14, 'stefcio@onet.pl', 'student has been added'),
        (1, 'Marian', 'Landryna', 12, 'marian@example.com', 'student has been added'),
    ])
    def test_system_add_student_parametrized_method(self, ipt1, ipt2, ipt3, ipt4, ipt5, expected):
        self.assertEqual(self.system.addStudent(ipt1, ipt2, ipt3, ipt4, ipt5), expected)


if __name__ == "__main__":
    unittest.main()
