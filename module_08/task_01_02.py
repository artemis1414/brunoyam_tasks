import sqlite3

con = sqlite3.connect('database_student.db')
con.execute("PRAGMA foreign_keys = 1")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY, 
            name VarChar(32), 
            surname VarChar(32), 
            age int, 
            city VarChar(32))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Courses (
            id INTEGER PRIMARY KEY, 
            name VarChar(32), 
            time_start text, 
            time_end text)""")

students = [(1, 'Max', 'Brooks', 24, 'Spb'),
            (2, 'John', 'Stones', 15, 'Spb'),
            (3, 'Andy', 'Wings', 45, 'Manchester'),
            (4, 'Kate', 'Brooks', 34, 'Spb')]
courses = [(1, 'python', '21.07.21', '21.08.21'),
           (2, 'java', '13.07.21', '16.08.21')]
# cur.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)",
#                 courses)
# cur.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)",
#                 students)
cur.execute("""CREATE TABLE IF NOT EXISTS Student_courses (
            student_id INTEGER NOT NULL,
            courses_id INTEGER NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Students (id)
            FOREIGN KEY (courses_id) REFERENCES Courses (id))""")
# cur.execute("INSERT INTO Student_courses (student_id, courses_id) VALUES (?, ?)", (1, 1))
# cur.execute("INSERT INTO Student_courses VALUES (?, ?)", (2, 1))
# cur.execute("INSERT INTO Student_courses VALUES (?, ?)", (3, 1))
# cur.execute("INSERT INTO Student_courses VALUES (?, ?)", (4, 2))
con.commit()
students_age_30 = cur.execute("""SELECT
                                    name, age 
                                FROM 
                                    Students 
                                WHERE 
                                    age > 30"""
                              ).fetchall()
students_python = cur.execute("""SELECT 
                                    Students.name, Courses.name  
                                FROM 
                                    Students, Courses, Students_courses 
                                WHERE 
                                    courses_id = Courses.id = 1 and student_id = Students.id"""
                              ).fetchall()
students_spb_p = cur.execute("""SELECT 
                                    Students.name, Courses.name, Students.city  
                                FROM 
                                    Students, Courses, Students_courses 
                                WHERE 
                                    courses_id = Courses.id = 1 and student_id = Students.id and Students.city = 'Spb'"""
                             ).fetchall()
print(students_age_30)
print(students_python)
print(students_spb_p)
con.close()
