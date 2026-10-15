from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import Student
from app.schema import StudentUpdate

router = APIRouter()

@router.put("/students/{student_id}")
def update_student(student_id: int,student: StudentUpdate,db: Session = Depends(get_db)):
    try:
        db_student = db.query(Student).filter(Student.id == student_id).first()

        if db_student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        update_data = student.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_student, key, value)

        db.commit()
        db.refresh(db_student)

        return db_student

    except Exception:
        db.rollback()
        raise
