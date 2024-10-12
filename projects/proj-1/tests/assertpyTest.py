from src.sample.sms import *
from assertpy import assert_that, fail


def test_error_msg_sysid():
    system = System()
    try:
        system.addStudent('11', 'Marek', 'Harasim', 15, 'marek@onet.pl')
    except Exception as e:
        assert_that(str(e)).is_equal_to('sysid not an int or student with this sysid already exists')


def test_error_msg_fname():
    system = System()
    try:
        system.addStudent(11, 0, 'Harasim', 15, 'marek@onet.pl')
    except Exception as e:
        assert_that(str(e)).is_equal_to('firstname not a string or empty string')


def test_error_msg_lname():
    system = System()
    try:
        system.addStudent(11, 'Marek', '', 15, 'marek@onet.pl')
    except Exception as e:
        assert_that(str(e)).is_equal_to('lastname not a string or empty string')


def test_error_msg_age():
    system = System()
    try:
        system.addStudent(11, 'Marek', 'Harasim', -3, 'marek@onet.pl')
    except Exception as e:
        assert_that(str(e)).is_equal_to('age not an int or less than 1')


def test_error_msg_email():
    system = System()
    try:
        system.addStudent(11, 'Marek', 'Harasim', 15, 0)
    except Exception as e:
        assert_that(str(e)).is_equal_to('email not a string')
