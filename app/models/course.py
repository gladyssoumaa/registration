from database import get_connection

def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                           course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL,
                           trainer_id INTEGER NOT NULL,
                           FOREIGN KEY (trsiner_id) REFERENCES trainers(trainer_id, first_name) ON DELETE CASCADE
                           )''')