from fastapi import APIRouter
from schemas.course import Courses
from repositories.course import(
    add_courses,
    list_courses,
    delete_course,
)
router = APIRouter(prefix="/courses", tags=["course"])


courses =[]

@router.post("")
def display_courses(course: Courses):
    add_courses(course.course_id, course.title, course.trainer_id, course.first_name)
    return {"message": "courses created", "course": Courses}

@router.get("/{course_id}")
def course(course_id: int):
    course= list_courses(course_id)
    return course

@router.delete("/{course_id}")
def delete_course_details(course: Courses):
    delete_course(course.course_id)
    return{"message": "deleted from records"}

