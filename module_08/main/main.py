from orm_sql import Base
import os

db = Base(os.environ['Base'])
db.create('Students', id='INTEGER PRIMARY KEY',  name='VarChar(32)', surname='VarChar(32)', age='int',
          city='VarChar(32)')
db.create('Courses', id='INTEGER PRIMARY KEY',  name='VarChar(32)', timestart='text', time_end='text')
db.create('Students_courses', student_id='INTEGER',  courses_id='INTEGER',
          FOREIGN=['FOREIGN KEY (student_id) REFERENCES Students (id)', 'FOREIGN KEY (courses_id) REFERENCES Courses (id)'])
# db.insert('Students', (1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
#                      (3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb'))
# db.insert('Courses', (1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21'))
# db.insert('Students_courses', (1, 1), (2, 1), (3, 1), (4, 2))
students_age_30 = db.select(['Students'], ['Students.name', 'Students.age'], 'age>30')
students_python = db.select(['Students', 'Courses', 'Students_courses'],
                            ['Students.name', 'Courses.name'],
                            'courses_id = Courses.id = 1 and student_id = Students.id')
student_spb_p = db.select(['Students', 'Courses', 'Students_courses'],
                          ['Students.name', 'Courses.name', 'Students.city'],
                          "courses_id = Courses.id = 1 and student_id = Students.id and Students.city = 'Spb'")
print(students_age_30)
print(students_python)
print(student_spb_p)

db.close()
