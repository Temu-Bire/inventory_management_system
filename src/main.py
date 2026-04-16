from fastapi import FastAPI
from .config import Settings
from .db.database import engine, Base
from .models import Product, Category, Supplier, StockMovement, User, Stock
from .api.product import router as product_router
from .api.catagory import router as category_router
from .api.suplier import router as supplier_router
from .api.stock import router as stock_router

settings=Settings()

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, description=settings.DESCRIPTION)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(supplier_router)
app.include_router(stock_router)

@app.on_event("startup")
async def startup_event():
    print("Starting application...")
    print("Creating database tables...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)  # Drop existing tables for a clean start
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully.")

@app.get("/")
async def read_root():
    return {"message": "Inventory system  is running!", "status": "OK"}
