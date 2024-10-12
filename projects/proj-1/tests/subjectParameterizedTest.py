import unittest
from parameterized import parameterized, parameterized_class
from src.sample.sms import *


@parameterized_class(('sysid', 'subject', 'expected_avg', 'added_subject'), [
    (13, 'Chemia', 3, 'student has been added to subject: Chemia'),
    (13, 'Fizyka', 4.5, 'student has been added to subject: Fizyka'),
    (13, 'Matematyka', 3, 'student has been added to subject: Matematyka'),
    (13, 'Biologia', 5, 'student has been added to subject: Biologia'),
    (13, 'Informatyka', 'subject has no grades', 'student has been added to subject: Informatyka'),
])
class SMSParameterized2(unittest.TestCase):

    def test_system_add_subject_parameterized_class(self):
        self.system.students = [{"age": 16,
                                 "comments": [],
                                 "email": "marek@buziaczek.pl",
                                 "firstname": "Marek",
                                 "lastname": "Harasim",
                                 "subjects": {},
                                 "sysid": 13}]
        self.assertEqual(self.system.addSubject(self.sysid, self.subject), self.added_subject)

    def test_system_stats_subject_parameterized_class(self):
        self.system.students = [{"age": 16,
                                 "comments": [],
                                 "email": "marek@buziaczek.pl",
                                 "firstname": "Marek",
                                 "lastname": "Harasim",
                                 "subjects": {"Chemia": [3],
                                              "Fizyka": [5, 4],
                                              "Matematyka":[2, 1, 6],
                                              "Biologia": [6, 5, 4],
                                              "Informatyka":[]},
                                 "sysid": 13}]
        self.assertEqual(self.system.statsSubject(self.sysid, self.subject), self.expected_avg)

    def setUp(self):
        self.system = System()


if __name__ == "__main__":
    unittest.main()



