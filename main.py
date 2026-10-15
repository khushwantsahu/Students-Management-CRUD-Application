from fastapi import FastAPI   
from app.database import engine,Base
from app.routes.base import api_router

Base.metadata.create_all(bind=engine)
app=FastAPI(
    title="Student Management System",
    description="This is a Student Management System API",
    version="1.0.0")

#app = FastAPI //we can also write this instead of the uper line
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message":"Welcome to Student Management System API"}