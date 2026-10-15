from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from app.schema import StudentResponse
from app.database import get_db
from app.model import Student

router = APIRouter(prefix="/students",tags=["Students"])

@router.get("/", response_model=list[StudentResponse])
def get_all_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students


@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student