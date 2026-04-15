from fastapi import FastAPI
from .config import Settings
from .db.database import engine, Base
from .models import Product, Category, Supplier, StockMovement, User, Stock

settings=Settings()

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, description=settings.DESCRIPTION)

@app.on_event("startup")
async def startup_event():
    print("Starting application...")
    print("Creating database tables...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully.")

@app.get("/")
async def read_root():
    return {"message": "Inventory system  is running!", "status": "OK"}
