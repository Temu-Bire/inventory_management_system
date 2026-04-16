from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.Suppliers import Supplier

class SupplierRepository:
    async def create(self, db: AsyncSession, data):
        supplier = Supplier(**data.dict())
        db.add(supplier)
        await db.commit()
        await db.refresh(supplier)
        return supplier

    async def get_all(self, db: AsyncSession):
        result = await db.execute(select(Supplier))
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, supplier_id: int):
        result = await db.execute(
            select(Supplier).where(Supplier.id == supplier_id)
        )
        return result.scalar_one_or_none()

    async def delete(self, db: AsyncSession, supplier):
        await db.delete(supplier)
        await db.commit()