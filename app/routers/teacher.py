from fastapi import APIRouter
from schemas.teacher import Teacher
from repositories.teacher import (
    add_trainer,
    get_trainer,
    update_trainer,
    delete_trainer,
)
router = APIRouter(prefix="/trainers", tags=["trainer"])


teachers =[]

@router.post("")
def register_trainer(teacher: Teacher):
    add_trainer(teacher.first_name, teacher.last_name, teacher.email, teacher.id_number, teacher.phone_number)
    return {"message": "Trainer added", "teacher": Teacher}

@router.get("")
def list_trainer(teacher: Teacher):
    teacher= get_trainer()
    return teacher

@router.put("/{trainer_id}")
def trainer_details(teacher: Teacher):
    update_trainer(teacher.first_name, teacher.last_name, teacher.email, teacher.id_number, teacher.phone_number)
    return{"message": "records updated"}

@router.delete("/{trainer_id}")
def delete_trainer_details(teacher: Teacher):
    delete_trainer(teacher.trainer_id)
    return{"message": "deleted from records"}

@router.get("{trainer_id}")
def trainer_details(trainer_id: int):
    teacher = get_trainer(trainer_id)
    return teacher