from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from ..config import Settings  

settings= Settings()
DATABASE_URL = settings.DATABASE_URL

# -----------------------------
# Engine (connection manager)
# -----------------------------
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # checks connections before using
    pool_size=5,          # number of connections
    max_overflow=10       # extra connections if needed
)

# -----------------------------
# Session factory
# -----------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# -----------------------------
# Base class for models
# -----------------------------
Base = declarative_base()

# -----------------------------
# Dependency (FastAPI)
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ Database connected successfully!")
    except Exception as e:
        print("❌ Database connection failed:", e)
if __name__ == "__main__":
    test_connection()