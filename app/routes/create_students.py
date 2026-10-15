from app.database import get_db
from app.model import Student
from app.schema import StudentCreate,StudentResponse
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/students",tags=["Students"])


@router.post("/",response_model=StudentResponse,status_code=status.HTTP_201_CREATED)

def create_student(student:StudentCreate,db:Session=Depends(get_db)):
    new_student=Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

