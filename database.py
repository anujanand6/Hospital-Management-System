import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER_NAME = "user"
PASSWORD = "123456"
DB_SCHEMA = "db_project"

# URL to connect to DB
SQLALCHEMY_DATABASE_URL = f"mysql://{USER_NAME}:{PASSWORD}@localhost/{DB_SCHEMA}"

# Create Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Initialize a DB session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
