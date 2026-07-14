from pydantic import BaseModel


class Teacher(BaseModel):
    first_name: str
    last_name: str
    email: str
    id_number: int
    phone_number: int