from database import get_connection

def add_trainer(first_name, last_name, email, id_number):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO trainers(first_name, last_name, email,id_number) VALUES (?,?,?,?)',
            (first_name, last_name, email, id_number),
        )

def get_trainer():
    with get_connection() as connection:
        connection.execute('SELECT * FROM trainers').fetchall()

def get_teacher(trainer_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers WHERE id = ?',(trainer_id,)).fetchone()

def update_trainer(first_name, last_name, email, id_number):
    with get_connection() as connection:
        connection.execute(
            'UPDATE students SET first_name=?, last_name=?, email=?,  id_number=? WHERE trainer_id=?',
            (first_name, last_name, email, id_number),
        )

def delete_trainer(trainer_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM trainers WHERE trainer_id = ?', (trainer_id,))