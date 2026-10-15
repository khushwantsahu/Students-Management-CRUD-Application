from app.routes import (
    create_students,
    delete_students,
    get_students,
    update_students,
    ai_query,
)
from fastapi import APIRouter
# master api to aggregate all inddivisual api route modules 
api_router = APIRouter()

api_router.include_router(create_students.router)
api_router.include_router(delete_students.router)
api_router.include_router(get_students.router)
api_router.include_router(update_students.router)
api_router.include_router(ai_query.app)