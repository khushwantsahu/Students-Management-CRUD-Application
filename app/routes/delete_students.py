from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import Student

router = APIRouter(prefix="/students",tags=["Students"])

@router.delete("/{student_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==student_id).first()
    if not student:
        return {"message":"Student not found"}
    db.delete(student)
    db.commit()
    return {"message":"Student deleted successfully"}