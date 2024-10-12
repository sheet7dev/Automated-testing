from src.sample.sms import *
import unittest


class SMSTest(unittest.TestCase):

    def setUp(self):
        self.system = System()

    def test_system_add_student(self):
        self.assertEqual(self.system.addStudent(11, 'Marek', 'Harasim', 16, 'marek@buziaczek.pl'), 'student has been '
                                                                                                   'added')

    def test_system_add_student_sysid_not_int(self):
        with self.assertRaises(Exception):
            self.system.addStudent('11', 'Marek', 'Harasim', 16, 'marek@buziaczek.pl')

    def test_system_add_student_sysid_already_exists(self):
        self.system.addStudent(11, 'Stefan', 'Stefański', 15, 'stefcio@onet.pl')
        with self.assertRaises(Exception):
            self.system.addStudent(11, 'Marek', 'Harasim', 16, 'marek@buziaczek.pl')

    def test_additional_exists_method_empty_list_of_students(self):
        self.assertFalse(self.system.exists(11))

    def test_additional_exists_method_student_exists(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 11}]
        self.assertTrue(self.system.exists(11))

    def test_system_add_student_firstname_not_str(self):
        with self.assertRaises(Exception):
            self.system.addStudent(11, 13, 'Harasim', 16, 'marek@buziaczek.pl')

    def test_system_add_student_firstname_pass_empty_str(self):
        with self.assertRaises(Exception):
            self.system.addStudent(11, '', 'Harasim', 16, 'marek@buziaczek.pl')

    def test_system_add_student_lastname_not_str(self):
        with self.assertRaises(Exception):
            self.system.addStudent(11, 'Marek', 13, 16, 'marek@buziaczek.pl')

    def test_system_add_student_lastname_pass_empty_str(self):
        with self.assertRaises(Exception):
            self.system.addStudent(11, 'Marek', '', 16, 'marek@buziaczek.pl')

    def test_system_add_student_age_not_int(self):
        with self.assertRaises(Exception):
            self.system.addStudent(11, 'Marek', 'Harasim', 'abc', 'marek@buziaczek.pl')

    def test_tsystem_add_student_age_less_than_one(self):
        with self.assertRaises(Exception):
            self.system.addStudent(11, 'Marek', 'Harasim', -5, 'marek@buziaczek.pl')

    def test_system_add_student_email_not_str(self):
        with self.assertRaises(Exception):
            self.system.addStudent(11, 'Marek', 'Harasim', 16, 0)

    def test_system_delete_student_one_student_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 11}]
        self.assertEqual(self.system.deleteStudent(11), 'deleted student with sysid: 11')

    def test_system_delete_student_sysid_not_in_list_of_students(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 11}]
        self.assertEqual(self.system.deleteStudent(13), 'student with sysid: 13 not exists')

    def test_system_delete_student_list_is_empty(self):
        self.assertEqual(self.system.deleteStudent(13), 'list is empty')

    def test_system_edit_student(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.editStudent(13, 'Stefan', 'Kasztan', 13, 'stefcio@onet.pl'), 'updated student '
                                                                                                  'with sysid: 13')

    def test_system_edit_student_sysid_not_in_list_of_students(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.editStudent(10, 'Stefan', 'Kasztan', 13, 'stefcio@onet.pl'), 'student with '
                                                                                                  'sysid: 10 not '
                                                                                                  'exists')

    def test_system_edit_student_firstname_not_str(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        with self.assertRaises(Exception):
            self.system.editStudent(13, 13, 'Harasim', 16, 'marek@buziaczek.pl')

    def test_system_edit_student_lastname_not_str(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        with self.assertRaises(Exception):
            self.system.editStudent(13, 'Marek', 13, 16, 'marek@buziaczek.pl')

    def test_system_edit_student_age_not_int(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        with self.assertRaises(Exception):
            self.system.editStudent(13, 'Marek', 'Harasim', '', 'marek@buziaczek.pl')

    def test_system_edit_student_email_not_str(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        with self.assertRaises(Exception):
            self.system.editStudent(13, 'Marek', 'Harasim', 16, 0)

    def test_system_edit_student_empty_list(self):
        self.assertEqual(self.system.editStudent(10, 'Marek', 'Harasim', 16, 'marek@buziaczek.pl'), 'list is empty')

    def test_system_add_subject(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.addSubject(13, 'Chemia'), 'student has been added to subject: Chemia')

    def test_sysytem_add_subject_sysid_not_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.addSubject(10, 'Fizyka'), 'student with sysid: 10 not exists')

    def test_system_add_subject_empty_list(self):
        self.assertEqual(self.system.addSubject(10, 'Biologia'), 'list is empty')

    def test_system_delete_subject(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.deleteSubject(13, 'Chemia'), 'student was released from the subject: Chemia')

    def test_system_delete_subject_sysid_not_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.deleteSubject(12, 'Chemia'), 'student with sysid: 12 not exists')

    def test_system_delete_subject_empty_list(self):
        self.assertEqual(self.system.deleteSubject(12, 'Chemia'), 'list is empty')

    def test_system_delete_subject_wrong_name_of_subject(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.deleteSubject(13, 'Fizyka'), 'student is not registered for this subject: Fizyka')

    def test_system_edit_subject(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.editSubject(13, 'Chemia', 'Fizyka'), 'Chemia has been renamed to Fizyka')

    def test_system_edit_subject_sysid_not_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.editSubject(11, 'Chemia', 'Fizyka'), 'student with sysid: 11 not exists')

    def test_system_edit_subject_empty_list(self):
        self.assertEqual(self.system.editSubject(13, 'Chemia', 'Fizyka'), 'list is empty')

    def test_system_edit_subject_wrong_subject_name(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.editSubject(13, 'Biologia', 'Fizyka'), 'student is not registered for this '
                                                                            'subject: Biologia')

    def test_system_add_grade_to_subject(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.addGradesSubject(13, 'Chemia', 4), 'grade: 4 has been added to subject: Chemia')

    def test_system_add_grade_to_subject_sysid_not_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.addGradesSubject(11, 'Chemia', 4), 'student with sysid: 11 not exists')

    def test_system_add_grade_to_subject_empty_list(self):
        self.assertEqual(self.system.addGradesSubject(11, 'Chemia', 4), 'list is empty')

    def test_system_add_grade_to_subject_subject_is_not_added(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.addGradesSubject(13, 'Chemia', 4), 'student is not registered for this subject: '
                                                                        'Chemia')

    def test_system_add_grade_to_subject_grade_more_than_6(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.addGradesSubject(13, 'Chemia', 7), 'given wrong value of grade: 7')

    def test_system_add_grade_to_subject_grade_less_than_1(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.addGradesSubject(13, 'Chemia', 0), 'given wrong value of grade: 0')

    def test_system_edit_grade(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.editGradesSubject(13, 'Chemia', 1, 5), 'grade has been changed')

    def test_system_edit_grade_sysid_not_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.editGradesSubject(11, 'Chemia', 1, 5), 'student with sysid: 11 not exists')

    def test_system_edit_grade_empty_list(self):
        self.assertEqual(self.system.editGradesSubject(11, 'Chemia', 1, 5), 'list is empty')

    def test_system_edit_grade_subject_is_not_added(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.editGradesSubject(13, 'Fizyka', 1, 5), 'student is not registered for this '
                                                                            'subject: Fizyka')

    def test_system_edit_grade_new_grade_less_than_1(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.editGradesSubject(13, 'Chemia', 1, -2), 'given wrong value of grade: -2')

    def test_system_edit_grade_new_grade_less_more_than_6(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.editGradesSubject(13, 'Chemia', 1, 8), 'given wrong value of grade: 8')

    def test_system_edit_grade_wrong_index(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.editGradesSubject(13, 'Chemia', -2, 4), 'provide the appropriate postition of '
                                                                             'grade')

    def test_system_add_comment(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.addComment(13, 'niegrzeczny na elekcji'), 'comment: niegrzeczny na elekcji, has '
                                                                               'been added')

    def test_system_add_comment_sysid_not_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.addComment(11, 'niegrzeczny na elekcji'), 'student with sysid: 11 not exists')

    def test_system_add_comment_empty_list(self):
        self.assertEqual(self.system.addComment(11, 'niegrzeczny na elekcji'), 'list is empty')

    def test_system_edit_comment(self):
        self.system.students = [{'age': 16,
                                 'comments': ['niegrzeczny na elekcji'],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.editComment(13, 1, 'nieobecny na elekcji'), 'comment has been changed')

    def test_system_edit_comment_sysid_not_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': ['niegrzeczny na elekcji'],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.editComment(11, 1, 'nieobecny na elekcji'), 'student with sysid: 11 not exists')

    def test_system_edit_comment_empty_list(self):
        self.assertEqual(self.system.editComment(11, 1, 'nieobecny na elekcji'), 'list is empty')

    def test_system_edit_comment_wrong_index(self):
        self.system.students = [{'age': 16,
                                 'comments': ['niegrzeczny na elekcji'],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {},
                                 'sysid': 13}]
        self.assertEqual(self.system.editComment(13, 2, 'nieobecny na elekcji'), 'provide the appropriate postition '
                                                                                 'of comment')

    def test_system_stats_of_subject(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3, 5]},
                                 'sysid': 13}]
        self.assertEqual(self.system.statsSubject(13, 'Chemia'), 4)

    def test_system_stat_of_subject_sysid_not_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.statsSubject(11, 'Chemia'), 'student with sysid: 11 not exists')

    def test_system_stat_of_subject_empty_list(self):
        self.assertEqual(self.system.statsSubject(11, 'Chemia'), 'list is empty')

    def test_system_stat_of_subject_subject_is_not_added(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.statsSubject(13, 'Fizyka'), 'student is not registered for this subject: Fizyka')

    def test_system_stat_of_subject_no_grades(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.statsSubject(13, 'Chemia'), 'subject has no grades')

    def test_system_stats_general(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3, 5], 'Fizyka': [5, 5]},
                                 'sysid': 13}]
        self.assertEqual(self.system.statsGeneral(13), 4.5)

    def test_system_stats_general_sysid_not_in_list(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.statsGeneral(11), 'student with sysid: 11 not exists')

    def test_system_stats_general_empty_list(self):
        self.assertEqual(self.system.statsGeneral(11), 'list is empty')

    def test_system_stats_general_all_subject_has_no_grades(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [], 'Fizyka': []},
                                 'sysid': 13}]
        self.assertEqual(self.system.statsGeneral(13), 'subjects has no grades')

    def test_system_save_students_data_to_file(self):
        self.system.students = [{'age': 16,
                                 'comments': [],
                                 'email': 'marek@buziaczek.pl',
                                 'firstname': 'Marek',
                                 'lastname': 'Harasim',
                                 'subjects': {'Chemia': [3]},
                                 'sysid': 13}]
        self.assertEqual(self.system.saveStudentsData('data/data.json'), 'data has been saved')

    def test_system_load_students_data_from_file(self):
        self.assertEqual(self.system.loadStudentsData('data/data.json'), 'data has been loaded')

    def test_system_load_students_data_from_file_wrong_path_or_file(self):
        self.assertEqual(self.system.loadStudentsData('data/dta.json'), 'wrong path or file')


if __name__ == "__main__":
    unittest.main()
