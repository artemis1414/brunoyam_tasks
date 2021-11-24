from module_08.main.orm_sql import Base
import unittest
from os import environ

students = [(1, 'Max', 'Brooks', 24, 'Spb'),
            (2, 'John', 'Stones', 15, 'Spb'),
            (3, 'Andy', 'Wings', 45, 'Manchester'),
            (4, 'Kate', 'Brooks', 34, 'Spb')]
courses = [(1, 'python', '21.07.21', '21.08.21'),
           (2, 'java', '13.07.21', '16.08.21')]
student_courses = [(1, 1),
                   (2, 1),
                   (3, 1),
                   (4, 2)]


class TestORM(unittest.TestCase):

    def setUp(self):
        self.orm = Base(environ['Base'])

    def test_create_tables(self):
        self.orm.create('Students', id='INTEGER PRIMARY KEY',  name='VarChar(32)', surname='VarChar(32)', age='int',
          city='VarChar(32)')
        self.orm.create('Courses', id='INTEGER PRIMARY KEY',  name='VarChar(32)', timestart='text', time_end='text')
        self.orm.create('Students_courses', student_id='INTEGER',  courses_id='INTEGER',
          FOREIGN=['FOREIGN KEY (student_id) REFERENCES Students (id)', 'FOREIGN KEY (courses_id) REFERENCES Courses (id)'])

    def test_insert_student(self):
        self.orm.insert('Students', *students)
        self.assertTrue(bool(self.orm.select(['Students'], ['Students.id'])))

    def test_insert_course(self):
        self.orm.insert('Courses', *courses)
        self.assertTrue(bool(self.orm.select(['Courses'], ['Courses.id'])))

    def test_insert_student_courses(self):
        self.orm.insert('Students_courses', *student_courses)

    def test_del_student(self):
        self.orm.delete('Students', 'id')
        self.assertFalse(bool(self.orm.select(['Students'], ['Students.id'])))

    def test_del_course(self):
        self.orm.delete('Courses', 'id')
        self.assertFalse(bool(self.orm.select(['Courses'], ['Courses.id'])))

