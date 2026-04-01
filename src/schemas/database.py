from sqlalchemy import create_engine
from ..config import settings

# Create database engine (connection manager)
engine = create_engine(settings.DATABASE_URL)


# Test connection (optional but recommended)
def test_connection():
    try:
        with engine.connect():
            print("✅ Database connected successfully!")
    except Exception as e:
        print("❌ Database connection failed:", e)
