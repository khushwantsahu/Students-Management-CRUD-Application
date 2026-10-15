from datetime import date
from typing import Optional
from pydantic import BaseModel

class StudentBase(BaseModel):
    student_name:str
    student_class:str
    student_section:str
    student_dob:date

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    student_name:Optional[str]=None
    student_class:Optional[str]=None
    student_section:Optional[str]=None
    student_dob:Optional[date]=None


class StudentResponse(StudentBase):
    id:int

    class Config:
        form_attributs=True
        