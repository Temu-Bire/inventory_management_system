from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.Schemas.category import *
from src.db.database import get_db
from src.services.catagory_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])
service = CategoryService()

@router.post("/", response_model=CategoryResponse)
async def create(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    return await service.create_category(db, category)

@router.get("/", response_model=list[CategoryResponse])
async def read_all(db: AsyncSession = Depends(get_db)):
    return await service.get_categories(db)

@router.get("/{category_id}", response_model=CategoryResponse)
async def read_one(category_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_category(db, category_id)


@router.delete("/{category_id}")
async def delete(category_id: int, db: AsyncSession = Depends(get_db)):
    return await service.delete_category(db, category_id)


