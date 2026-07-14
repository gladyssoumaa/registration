from pydantic import BaseModel

class Courses(BaseModel):
    course_id: int
    title: str
    trainer_id: int