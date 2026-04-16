# api/product.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.Schemas.product import *
from src.db.database import get_db
from src.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])
service = ProductService()


@router.post("/", response_model=ProductResponse)
async def create(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await service.create_product(db, product)


@router.get("/", response_model=list[ProductResponse])
async def read_all(db: AsyncSession = Depends(get_db)):
    return await service.get_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
async def read_one(product_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_product(db, product_id)


@router.put("/{product_id}", response_model=ProductResponse)
async def update(product_id: int, data: ProductUpdate, db: AsyncSession = Depends(get_db)):
    return await service.update_product(db, product_id, data)


@router.delete("/{product_id}")
async def delete(product_id: int, db: AsyncSession = Depends(get_db)):
    return await service.delete_product(db, product_id)