from database import get_connection


def add_courses(title, trainer_id, first_name):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses(title, trainer_id, first_name) VALUES (?,?,?)',
            (title, trainer_id, first_name),
        )

def list_courses():
    with get_connection() as connection:
        connection.execute('SELECT(title, trainer_id, first_name) * FROM courses').fetchall()

def list_course(course_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses WHERE id = ?',(course_id,)).fetchone()

def delete_course(course_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM courses WHERE course_id = ?', (course_id,))      
