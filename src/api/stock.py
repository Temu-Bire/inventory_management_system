from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.Schemas.Stock import *
from src.db.database import get_db
from src.services.stock_service import StockService

router = APIRouter(prefix="/stock", tags=["Stock"])
service = StockService()

@router.post("/", response_model=StockResponse)
async def create(stock: StockCreate, db: AsyncSession = Depends(get_db)):
    return await service.create_stock(db, stock)

@router.get("/", response_model=list[StockResponse])
async def read_all(db: AsyncSession = Depends(get_db)):
    return await service.get_stock(db)

@router.get("/{stock_id}", response_model=StockResponse)
async def read_one(stock_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_stock_by_id(db, stock_id)

@router.delete("/{stock_id}")
async def delete(stock_id: int, db: AsyncSession = Depends(get_db)):
    return await service.delete_stock(db, stock_id)
