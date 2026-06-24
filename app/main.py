from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table, add_student, get_students, add_trainer, get_trainer, add_courses, list_courses, delete_student, delete_course, delete_trainer, update_students, update_trainer,delete_course

app = FastAPI()
create_table()

@app.get("/")
def home():
    return {"message": "Welcome to my API server"}


students = []

class Student(BaseModel):
    name:str
    age:int
    email:str
    country:str
    id_number:int
    reg_number: int


@app.get("/students")
def list_students():
    students = get_students()
    return students


@app.post("/students")
def register_student(student:Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number, student.reg_number)
    return{"Message": "Student registered", "student":Student}

@app.put("/students/{student_id}")
def student_details(student: Student):
    update_students(student.name, student.age,student.email, student.country, student.id_number, student.reg_number)
    return{"message": "records updated"}

@app.delete("/students/{student_id}")
def delete_student_details(student: Student):
    delete_student(student.student_id)
    return{"message": "deleted from records"}


class Teacher(BaseModel):
    first_name: str
    last_name: str
    email: str
    id_number: int
    phone_number: int

teachers =[]

@app.post("/trainers")
def register_trainer(teacher: Teacher):
    add_trainer(teacher.first_name, teacher.last_name, teacher.email, teacher.id_number, teacher.phone_number)
    return {"message": "Trainer added", "teacher": Teacher}

@app.get("/trainers")
def list_trainer(teacher: Teacher):
    teacher= get_trainer
    return teacher

@app.put("/trainers/{trainer_id}")
def trainer_details(teacher: Teacher):
    update_trainer(teacher.first_name, teacher.last_name, teacher.email, teacher.id_number, teacher.phone_number)
    return{"message": "records updated"}

@app.delete("/trainers/{trainer_id}")
def delete_trainer_details(teacher: Teacher):
    delete_trainer(teacher.trainer_id)
    return{"message": "deleted from records"}




class Courses(BaseModel):
    course_id: int
    title: str
    trainer_id: int

courses =[]

@app.post("/courses")
def display_courses(course: Courses):
    add_courses(course.course_id, course.title, course.trainer_id, course.first_name)
    return {"message": "courses created", "course": Courses}

@app.get("/courses")
def course(course: Courses):
    course= list_courses
    return course

@app.delete("/courses/{course_id}")
def delete_course_details(course: Courses):
    delete_course(course.course_id)
    return{"message": "deleted from records"}
