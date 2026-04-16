from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.Schemas.Supplier import *
from src.db.database import get_db
from src.services.suplier_service import SupplierService

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])
service = SupplierService()

@router.post("/", response_model=SupplierResponse)
async def create(supplier: SupplierCreate, db: AsyncSession = Depends(get_db)):
    return await service.create_supplier(db, supplier)

@router.get("/", response_model=list[SupplierResponse])
async def read_all(db: AsyncSession = Depends(get_db)):
    return await service.get_suppliers(db)

@router.get("/{supplier_id}", response_model=SupplierResponse)
async def read_one(supplier_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_supplier(db, supplier_id)

@router.delete("/{supplier_id}")
async def delete(supplier_id: int, db: AsyncSession = Depends(get_db)):
    return await service.delete_supplier(db, supplier_id)