import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager
def get_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           country TEXT NOT NULL,
                           id_number INTEGER NOT NULL,
                           reg_number INTEGER NOT NULL
                           )''')
        connection.execute('''CREATE TABLE IF NOT EXISTS trainers(
                           trainer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           first_name TEXT NOT NULL,
                           last_name TEXT NOT NULL,
                           email TEXT NOT NULL,
                           id_number INTEGER NOT NULL
                           )''')
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                           course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL,
                           trainer_id INTEGER NOT NULL,
                           FOREIGN KEY (trsiner_id) REFERENCES trainers(trainer_id, first_name) ON DELETE CASCADE
                           )''')
        
def add_student(name, age, email, country, id_number, reg_number):
    with get_connection() as connection:
        connection.execute(
        'INSERT INTO students(name, age, email, country, id_number, reg_number) VALUES (?,?,?,?,?)',
        (name, age, email, country, id_number, reg_number),
    )

def get_students():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()
    
def update_students(name, age, email, country, id_number, student_id, reg_number):
    with get_connection() as connection:
        connection.execute(
            'UPDATE students SET name=?, age=?, email=?, country=?, id_number=?, reg_number=? WHERE student_id=?',
            (name, age, email, country, id_number, student_id, reg_number),
        )

def delete_student(student_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM students WHERE id = ?', (student_id,))

def add_trainer(first_name, last_name, email, id_number):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO trainers(first_name, last_name, email,id_number) VALUES (?,?,?,?)',
            (first_name, last_name, email, id_number),
        )

def get_trainer():
    with get_connection() as connection:
        connection.execute('SELECT * FROM trainers').fetchall()

def update_trainer(first_name, last_name, email, id_number):
    with get_connection() as connection:
        connection.execute(
            'UPDATE students SET first_name=?, last_name=?, email=?,  id_number=? WHERE trainer_id=?',
            (first_name, last_name, email, id_number),
        )

def delete_trainer(trainer_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM trainers WHERE trainer_id = ?', (trainer_id,))


def add_courses(title, trainer_id, first_name):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses(title, trainer_id, first_name) VALUES (?,?,?)',
            (title, trainer_id, first_name),
        )

def list_courses():
    with get_connection() as connection:
        connection.execute('SELECT(title, trainer_id, first_name) * FROM courses').fetchall()

def delete_course(course_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM courses WHERE course_id = ?', (course_id,))      

