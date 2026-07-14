from fastapi import APIRouter
from schemas.student import Student
from repositories.student import(
    get_students,
    add_student,
    update_students,
    delete_student,
)
router = APIRouter(prefix="/students", tags=["students"])


students = []

@router.get("")
def list_students():
    students = get_students()
    return students


@router.post("")
def register_student(student:Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number, student.reg_number)
    return{"Message": "Student registered", "student":Student}

@router.put("/{student_id}")
def student_details(student: Student):
    update_students(student.name, student.age, student.email, student.country, student.student_id, student.reg_number)
    return{"message": "records updated"}

@router.delete("/{student_id}")
def delete_student_details(student: Student):
    delete_student(student.student_id)
    return{"message": "deleted from records"}

@router.get("/{student_id}")
def student_detail(student_id: int):
    student = get_students(student_id)
    return student