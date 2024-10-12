from src.sample.sms import *
from hamcrest import *
import unittest


class SMSHamcrestTest(unittest.TestCase):
    def test_len_of_students_list(self):
        self.system.addStudent(10, 'Stefan', 'Kasztan', 14, 'kasztanki@o2.pl')
        self.system.addStudent(11, 'Marek', 'Harasim', 15, 'marek@onet.pl')
        assert_that(self.system.students, has_length(2))

    def test_sysid_not_an_int(self):
        assert_that(calling(self.system.addStudent).with_args('11'), raises(Exception))

    def test_fname_not_a_str(self):
        assert_that(calling(self.system.addStudent).with_args(11, 2), raises(Exception))

    def test_lname_not_a_str(self):
        assert_that(calling(self.system.addStudent).with_args(11, 'Marek', 0), raises(Exception))

    def test_age_not_an_int(self):
        assert_that(calling(self.system.addStudent).with_args(11, 'Marek', 'Harasim', ''), raises(Exception))

    def test_age_less_than_one(self):
        assert_that(calling(self.system.addStudent).with_args(11, 'Marek', 'Harasim', -3), raises(Exception))

    def setUp(self):
        self.system = System()


if __name__ == "__main__":
    unittest.main()