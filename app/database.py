from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

# Basic validation for DATABASE_URL
if not DATABASE_URL or not DATABASE_URL.startswith(("postgresql://", "mysql://", "sqlite://")):
    # Defaulting to a local sqlite database for development if URL is missing or invalid
    DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()