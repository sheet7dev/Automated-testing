import json


class Student:
    def __init__(self, sysid, firstname, lastname, age, email, subjects, comments):
        self.sysid = sysid
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.subjects = subjects
        self.comments = comments


class System:
    def __init__(self):
        self.students = []

    # student

    def addStudent(self, sysid, firstname, lastname, age, email):
        if type(sysid) is int and self.exists(sysid) is False:
            if type(firstname) is str and len(firstname) != 0:
                if type(lastname) is str and len(lastname) != 0:
                    if type(age) is int and age > 0:
                        if type(email) is str:
                            newStudent = Student(sysid, firstname, lastname, age, email, subjects={}, comments=[])
                            mydict = {'sysid': newStudent.sysid,
                                      'firstname': newStudent.firstname,
                                      'lastname': newStudent.lastname,
                                      'age': newStudent.age,
                                      'email': newStudent.email,
                                      'subjects': newStudent.subjects,
                                      'comments': newStudent.comments}
                            self.students.append(mydict)
                            return 'student has been added'
                        else:
                            raise Exception('email not a string')
                    else:
                        raise Exception('age not an int or less than 1')
                else:
                    raise Exception('lastname not a string or empty string')
            else:
                raise Exception('firstname not a string or empty string')
        else:
            raise Exception('sysid not an int or student with this sysid already exists')

    def exists(self, sysid):
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    return True
                else:
                    return False
        else:
            return False

    def deleteStudent(self, sysid):
        if len(self.students) != 0:
            index = -1
            for student in self.students:
                index += 1
                if student['sysid'] == sysid:
                    del self.students[index]
                    return f'deleted student with sysid: {sysid}'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    def editStudent(self, sysid, firstname, lastname, age, email):
        if len(self.students) != 0:
            for student in self.students:
                if type(firstname) is str and type(lastname) is str and type(age) is int and age > 0 and type(
                        email) is str:
                    if student['sysid'] == sysid:
                        student['firstname'] = firstname
                        student['lastname'] = lastname
                        student['age'] = age
                        student['email'] = email
                        return f'updated student with sysid: {sysid}'
                    else:
                        return f'student with sysid: {sysid} not exists'
                else:
                    raise Exception('given wrong value')
        else:
            return 'list is empty'

    # subject

    def addSubject(self, sysid, subject):
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    student['subjects'][subject] = []
                    return f'student has been added to subject: {subject}'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    def deleteSubject(self, sysid, subject):
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    try:
                        del student['subjects'][subject]
                        return f'student was released from the subject: {subject}'
                    except KeyError:
                        return f'student is not registered for this subject: {subject}'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    def editSubject(self, sysid, subject, edited_subject):
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    try:
                        student['subjects'][edited_subject] = student['subjects'][subject]
                        del student['subjects'][subject]
                        return f'{subject} has been renamed to {edited_subject}'
                    except KeyError:
                        return f'student is not registered for this subject: {subject}'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    # grades

    def addGradesSubject(self, sysid, subject, grade):
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    try:
                        if 1 <= grade <= 6:
                            student['subjects'][subject].append(grade)
                            return f'grade: {grade} has been added to subject: {subject}'
                        else:
                            raise ValueError
                    except KeyError:
                        return f'student is not registered for this subject: {subject}'
                    except ValueError:
                        return f'given wrong value of grade: {grade}'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    def editGradesSubject(self, sysid, subject, grade_index, new_grade):
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    try:
                        if 1 <= new_grade <= 6:
                            student['subjects'][subject][grade_index - 1] = new_grade
                            return 'grade has been changed'
                        else:
                            raise ValueError
                    except KeyError:
                        return f'student is not registered for this subject: {subject}'
                    except ValueError:
                        return f'given wrong value of grade: {new_grade}'
                    except IndexError:
                        return 'provide the appropriate postition of grade'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    # comments

    def addComment(self, sysid, comment):
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    student['comments'].append(comment)
                    return f'comment: {comment}, has been added'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    def editComment(self, sysid, comment_index, new_comment):
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    try:
                        student['comments'][comment_index - 1] = new_comment
                        return 'comment has been changed'
                    except IndexError:
                        return 'provide the appropriate postition of comment'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    # stats

    def statsSubject(self, sysid, subject):
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    try:
                        grades = student['subjects'][subject]
                        avg = sum(grades) / len(grades)
                        return avg
                    except KeyError:
                        return f'student is not registered for this subject: {subject}'
                    except ZeroDivisionError:
                        return 'subject has no grades'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    def statsGeneral(self, sysid):
        avg = 0
        no_grades = 0
        acc = 0
        if len(self.students) != 0:
            for student in self.students:
                if student['sysid'] == sysid:
                    try:
                        for grade in student['subjects'].values():
                            if len(grade) != 0:
                                acc += sum(grade) / len(grade)
                            else:
                                no_grades += 1
                            avg = acc / (len(student['subjects']) - no_grades)
                        return avg
                    except ZeroDivisionError:
                        return 'subjects has no grades'
                else:
                    return f'student with sysid: {sysid} not exists'
        else:
            return 'list is empty'

    # data/ json file

    def saveStudentsData(self, path):
        with open(path, 'w') as file:
            json.dump(self.students, file)
        return 'data has been saved'

    def loadStudentsData(self, path):
        try:
            with open(path, 'r') as file:
                students_data = file.read()
            self.students = json.loads(students_data)
            return 'data has been loaded'
        except FileNotFoundError:
            return 'wrong path or file'
