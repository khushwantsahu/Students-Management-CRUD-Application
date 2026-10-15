from app.config import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL=Settings.database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False});
sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
